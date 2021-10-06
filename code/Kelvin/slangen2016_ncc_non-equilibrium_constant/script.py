import csv
import numpy as np
import matplotlib.pyplot as plt
import array
import pandas as pd
from scipy import stats
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

t,z,names = st.load_gm_steric('historical') ## Get CMIP6 historical steric data

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

z[z>1e10] = np.nan      ## Set missing values to nan
z[z<-1e10] = np.nan     ## Set missing values to nan

## Reference to 1992-2014 mean, to match OBS data
ref_index = np.where((t>=ybl_st) & (t<ybl_ed+1))
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
rind, = np.where((cmip_year_axis>=yta_st) &
            (cmip_year_axis<=yta_ed))
z_cmip = z_cur_an[rind,:]
## Load historical observation from the Frederikse SLB data
## Data range: 1900-2018
## The values are relative to the 2002-2018 mean
hist_slb_raw = pd.read_csv('~/project01/data/raw_data/frederikse_SLB_data.txt', delim_whitespace=True, header=0)
hist_steric = np.array(hist_slb_raw.steric) ## To numpy array
hist_year_axis = np.array(range(1900,2019)) ## Subsitute year axis
ref_index, = np.where((hist_year_axis>=ybl_st) & (hist_year_axis<ybl_ed+1))
## Calculate the anomaly with the given baseline value
hist_steric = hist_steric - np.mean(hist_steric[ref_index])

rind, = np.where((hist_year_axis>=yta_st) &
            (hist_year_axis<=yta_ed))

hist_steric = hist_steric[rind]
onoff=0

## Now we calculate two things
## (1) Mean difference btween the modelled and observed steric (1970-2005)
## (2) Residual trends over the period 1970-2005

for j in range(0,len(name_unique)):
    tind = names.index[names["model"]==name_unique[j]] ## Get the target index
    print("---------------------")
    tind = tind - 1
    for k in range(0,len(tind)):
        cur_name = names.iloc[tind[k]]['model']
        cur_run = names.iloc[tind[k]]['run']
        dum_a = cur_run.split("_")
        dum_b = dum_a[0].split("p")
        dum_c = dum_b[1].split("f")
        model_p = dum_c[0]
        model_f = dum_c[1]
        nmissing = sum(np.isnan(z_cmip[:,tind[k]]))
        print(cur_name+" "+cur_run+" "+str(nmissing))
## Calculate steric obs - steric model 1970-2005 mm
        tmp = hist_steric - z_cmip[:,tind[k]]   ## Residual
        tmp_a = np.nanmean(tmp)                 ## Mean residual

## Calculate slope of diff(steric_obs - steric model) vs YEAR
        dum_time = np.array(range(1970,2006))
        mask = ~np.isnan(z_cmip[:,tind[k]]) ## Only use data that is not nan
        slope,intercept, r, p, se = stats.linregress(dum_time[mask],tmp[mask])
        if onoff == 0:
            tmp_diff = tmp_a
            tmp_slope = slope
            tmp_intercept = intercept
            tmp_name = cur_name
            tmp_run = cur_run
            tmp_missing = nmissing
            tmp_p = model_p
            tmp_f = model_f
            onoff = 1
        else:
            tmp_diff = np.append(tmp_diff,tmp_a)
            tmp_slope = np.append(tmp_slope,slope)
            tmp_intercept = np.append(tmp_intercept,intercept)
            tmp_name = np.append(tmp_name,cur_name)
            tmp_run = np.append(tmp_run,cur_run)
            tmp_missing = np.append(tmp_missing,nmissing)
            tmp_p = np.append(tmp_p,model_p)
            tmp_f = np.append(tmp_f,model_f)
## Create output dataframe
output_pd = {'model': tmp_name,
        'run': tmp_run,
        'model_p':tmp_p,
        'model_f':tmp_f,
        'odm': tmp_diff,
        'grad':tmp_slope,
        'intercept':tmp_intercept,
        'num_nan':tmp_missing}
output_fin = pd.DataFrame(output_pd)
output_fin.to_csv('raw_stat.csv',mode='a',sep=",",index=False)
