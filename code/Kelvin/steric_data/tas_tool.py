import csv
import numpy as np
import matplotlib.pyplot as plt
import array
import pandas as pd
import os.path

def load_tas_cmip6(model_name,run_name,scenario):
    root_path = 'project01/data/raw_data/cmip6_tas_for_steric_analysis'
    ## Check whether historical file exist
    hist_path = root_path+'/historical/gm_tas_CMIP_historical_'+model_name+'_'+run_name+'.csv'
    if os.path.isfile(hist_path):
    ## Read historical first
        hist_tmp = pd.read_csv(hist_path,sep=',',names=['time','tas'],header=0)
    ## Read SSP
        ssp_path = root_path+'/'+scenario+'/gm_tas_ScenarioMIP_'+scenario+'_'+model_name+'_'+run_name+'.csv'
        if os.path.isfile(ssp_path):
            ssp_tas = pd.read_csv(ssp_path,sep=',',names=['time','tas'],header=0)
            hist_tmp = hist_tmp.append(ssp_tas)
    else:
        hist_tmp = pd.array([1])
    return(hist_tmp)

if __name__ == "__main__":
    ttt = load_tas_cmip6('NESM3','r1i1p1f1_gn','ssp585')
    print(ttt)
