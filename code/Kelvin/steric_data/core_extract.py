import csv
import numpy as np
import matplotlib.pyplot as plt
import array
import pandas as pd
from scipy import stats
import steric_tools as st
import tas_tool as tt

## scenario: CMIP scenario
## yta_st : Time range start [Inclusive]
## yta_ed : Time range end [Inclusive]
## ybl_st : Baseline period start [Inclusive]
## ybl_ed : Baseline period end [Inclusive]
## onoff : Flag

def extract_steric_v1(scenario,yta_st,yta_ed,ybl_st,ybl_ed,onoff=0):
##=============================================================================
## Main script
## Get CMIP6 historical steric data
## For historical, the values are relative to Jan 2000 [Disabled]. Range: 1801-2040
## For Scen, the values are relative to Jan 2020 [Disabled]. Range: 2001-2310
    t,z,names = st.load_gm_steric(scenario)
## Structure
## names : (177, 2), index 2: 0 = model, 1 = run [ensemble/setup]
## t : (2880,), Time: Middle of the month (start from 1/24 with 2/24 incre)
## z : (2880, 177), index 1: Time, index 2: names
## List of unique models
    name_unique = sorted(set(names.model))
    z = np.where(np.abs(z)>10**5,np.nan,z)  ## Remove super fishy entries
    z = z*1e3   ## m to mm
    n_z = z.shape
    n_runs = n_z[1]
    n_time = n_z[0]
    model_name = names.model
    run_name = names.run
    z_cmip_s = z[np.where((t>=yta_st)&(t<yta_st+1)),:]
    z_cmip_s = z_cmip_s[0,:,:]
    z_cmip_e = z[np.where((t>=yta_ed)&(t<yta_ed+1)),:]
    z_cmip_e = z_cmip_e[0,:,:]
## Check whether tas file exists for that particular run
    count = 0
    for i in range(0,n_runs):
        #print("**************************************")
        print("Current :",model_name.iloc[i],run_name.iloc[i])
        if scenario == "historical":
            tas_cmip = tt.load_tas_cmip6(model_name.iloc[i],run_name.iloc[i],'ssp126')
        else:
            tas_cmip = tt.load_tas_cmip6(model_name.iloc[i],run_name.iloc[i],scenario)
        if len(tas_cmip.shape) == 1:
            print(" >>>>> NO historical TAS: "+model_name.iloc[i]+" "+run_name.iloc[i],"<<<<<<")
        else:            ## Continue if the tas file exists
# For checking
#            count = count + 1
#            next                        
            tas_time = np.array(tas_cmip.time)
            tas_time = tas_time / 100           ## Now it is in decimal form, i.e. yyyy.mm
            tas_actu = np.array(tas_cmip.tas)
## Calculate baseline value
            tas_bl = tas_actu[np.where((tas_time>=ybl_st)&(tas_time<ybl_ed+1))]
            tas_bl_avg = tas_bl.mean()
## Extract TAS within the target range
            tas_ta = tas_actu[np.where((tas_time>=yta_st)&(tas_time<yta_ed+1))]
            tas_ta_avg = tas_ta.mean()
            tas_ta_avg = tas_ta_avg - tas_bl_avg    ## reference to baseline period

## Extract Steric height
            tmp_zavg_e = np.nanmean(z_cmip_e[:,i])
            tmp_zavg_s = np.nanmean(z_cmip_s[:,i])
            tmp_zavg = (tmp_zavg_e - tmp_zavg_s) / (yta_ed - yta_st+1)
            if tmp_zavg == 0:
                print("----------------------------------")
                print(tmp_zavg_e,tmp_zavg_s)
                print(z_cmip_e[:,i])
                print(z_cmip_s[:,i])
                tmp_zavg = np.nan 
            if onoff == 0:
                out_comp = 'steric'
                out_source = 'CMIP6_RB'
                out_model = model_name.iloc[i]
                out_run = run_name.iloc[i]
                out_scenaro = scenario
                out_styr = yta_st
                out_edyr = yta_ed
                out_temp = tas_ta_avg
                out_zavg = tmp_zavg
                onoff = 1
            else:
                out_comp = np.append(out_comp,'steric')
                out_source = np.append(out_source,'CMIP6_RB')
                out_model = np.append(out_model,model_name.iloc[i])
                out_run = np.append(out_run,run_name.iloc[i])
                out_scenaro = np.append(out_scenaro,scenario)
                out_styr = np.append(out_styr,yta_st)
                out_edyr = np.append(out_edyr,yta_ed)
                out_temp = np.append(out_temp,tas_ta_avg)
                out_zavg = np.append(out_zavg,tmp_zavg)

    output_pd = {'Component':out_comp,
            'Source':out_source,
            'CMIPModel':out_model,
            'Run':out_run,
            'Scenario':out_scenaro,
            'startyr':out_styr,
            'endyr':out_edyr,
            'Tavg':out_temp,
            'dSdt':out_zavg}
    output_fin = pd.DataFrame(output_pd) 
    return(output_fin)
#    print("Total :"+str(count)+"/"+str(n_runs))

if __name__ == "__main__":
    ybl_st = 1995
    ybl_ed = 2014
#    yta_st = 1850
#    yta_ed = 1900
    yta_st = 2016
    yta_ed = 2050
    kappa = extract_steric_v1('ssp585',yta_st,yta_ed,ybl_st,ybl_ed)
    print(kappa)

