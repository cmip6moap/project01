import csv
import numpy as np
import matplotlib.pyplot as plt
import array
import pandas as pd
from scipy import stats
##from scipy.ndimage import median_filter  # used for outlier removal
import steric_tools as st

##=============================================================================
## INPUT
## Baseline years
ybl_st = 1992
ybl_ed = 2014

## Target range
yta_st = 1970
yta_ed = 2005

##=============================================================================
## Main script
## Get CMIP6 historical steric data
## For historical, the values are relative to Jan 2000 [Disabled]. Range: 1801-2040 
## For Scen, the values are relative to Jan 2020 [Disabled]. Range: 2001-2310

t,z,names = st.load_gm_steric('historical')
## Structure
## names : (177, 2), index 2: 0 = model, 1 = run [ensemble/setup]
## t : (2880,), Time: Middle of the month (start from 1/24 with 2/24 incre)
## z : (2880, 177), index 1: Time, index 2: names

## List of unique models
name_unique = sorted(set(names.model))
z = z*1e3   ## m to mm
n_z = z.shape
n_runs = n_z[1]
n_time = n_z[0]

## Reference to 1992-2014 mean, to match OBS data
ref_index = np.where((t>=ybl_st) & (t<=ybl_ed+1)) ## +1 to cover the final year
z_cur = z
for i in range(0,n_runs):
    z_cur[:,i] = z_cur[:,i] - np.nanmean(z[ref_index,i])

## Calculate annual mean
n_year = 2040-1801 + 1
z_cur_an=np.empty((n_year,n_runs))
z_cur_an[:]=np.nan
for j in range(0,n_runs):
    for i in range(1801,2041):
        z_cur_an[i-1801,j] = np.nanmean(z_cur[np.where((t>i) & (t<i+1)),j])

cmip_year_axis = np.array(range(1801,2041))
## Extract target range for calculation
z_cmip = z_cur_an[np.where((cmip_year_axis>=yta_st) &
            (cmip_year_axis<=yta_ed)),:]
z_cmip = z_cmip[0,:,:]

## Load historical observation from the Frederikse SLB data
## Data range: 1900-2018
## The values are relative to the 2002-2018 mean
hist_slb_raw = pd.read_csv('../../../../data/raw_data/frederikse_SLB_data.txt', delim_whitespace=True, header=0)
hist_steric = np.array(hist_slb_raw.steric) ## To numpy array
hist_year_axis = np.array(range(1900,2019)) ## Subsitute year axis
ref_index = np.where((hist_year_axis>ybl_st) & (hist_year_axis<ybl_ed))
## Calculate the anomaly with the given baseline value
hist_steric = hist_steric - np.mean(hist_steric[ref_index])
hist_steric = hist_steric[np.where((hist_year_axis>=yta_st) &
            (hist_year_axis<=yta_ed))]

## Create flag
## 0 : Normal
## 1 : All nan in the array
## 2 : There is at least one entry with value larger than 1000
flag=np.zeros(n_runs)
for j in range(0,n_runs):
    if np.isnan(z_cmip[:,j]).all():
        print(names.model[j]+" Empty series")
        flag[j]=1
    if any(abs(i) > 1000 for i in z_cmip[:,j]):
        print(names.model[j]+" Unrealistic number")
        flag[j]=2

z_diff_median = np.empty(len(name_unique))
z_slope_median = np.empty(len(name_unique))
onoff=0
for j in range(0,len(name_unique)):
    tind = names.index[names["model"]==name_unique[j]] ## Get the target index
    print("---------------------")
    tind = tind - 1
    for k in range(0,len(tind)):
        #print(names.iloc[tind[k]]['model']+" "+names.iloc[tind[k]]['run'])
        if flag[tind[k]]!=0:    ## Skip if funny things occurred
            continue
        cur_name = names.iloc[tind[k]]['model']
        cur_run = names.iloc[tind[k]]['run']
        print(cur_name+" "+cur_run)

## Get time range
        dum_time = np.array(range(yta_st,yta_ed+1))
        mask = ~np.isnan(z_cmip[:,tind[k]])         ## Only want indices of non nan values

## Calculate pearson r between steric obs and steric model 1970-2005 mm
        pcor_r, pcor_pval = stats.pearsonr(hist_steric[mask],z_cmip[mask,tind[k]])

## KS test
        ks_stat, ks_pval = stats.ks_2samp(hist_steric[mask],z_cmip[mask,tind[k]])

## Calculate steric obs - steric model 1970-2005 mm
        diff_obsc = hist_steric - z_cmip[:,tind[k]]
        diff_obsa = np.nanmean(diff_obsc)   ## Mean difference
## Gradient of residual change 
        rslope, rintercept, rr, rp, rse = stats.linregress(dum_time[mask],diff_obsc[mask])

## Calculate slope of steric model vs time
        cslope,cintercept, cr, cp, cse = stats.linregress(dum_time[mask],z_cmip[mask,tind[k]])
        if onoff == 0:
            tmp_rslope = rslope
            tmp_diff_obsa = diff_obsa
            tmp_slope = cslope
            tmp_r = pcor_r
            tmp_p = pcor_pval
            tmp_name = cur_name
            tmp_run = cur_run
            tmp_ks_stat = ks_stat
            tmp_ks_pval = ks_pval
            onoff = 1
        else:
            tmp_rslope = np.append(tmp_rslope,rslope)
            tmp_diff_obsa = np.append(tmp_diff_obsa,diff_obsa)
            tmp_slope = np.append(tmp_slope,cslope)
            tmp_r = np.append(tmp_r,pcor_r)
            tmp_p = np.append(tmp_p,pcor_pval)
            tmp_name = np.append(tmp_name,cur_name)
            tmp_run = np.append(tmp_run,cur_run)
            tmp_ks_stat = np.append(tmp_ks_stat,ks_stat)
            tmp_ks_pval = np.append(tmp_ks_pval,ks_pval)
## Create output dataframe
output_pd = {'model': tmp_name,
        'run': tmp_run,
        'lin_grad':tmp_slope,
        'r':tmp_r,
        'p':tmp_p,
        'mean_omm':tmp_diff_obsa,
        'resid_grad':tmp_rslope,
        'ks_stat':tmp_ks_stat,
        'ks_pval':tmp_ks_pval}
output_fin = pd.DataFrame(output_pd)
print(output_fin)
#exit()
output_fin.to_csv('raw_stat_v2.csv',mode='a',sep=",")
