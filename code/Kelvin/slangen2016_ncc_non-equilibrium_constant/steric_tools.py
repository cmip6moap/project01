"""
Based on rory binghams example code.

Modified by Aslak Grinsted 2021
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import array
import pandas as pd
from scipy.ndimage import median_filter  # used for outlier removal



def load_gm_steric(scenario = 'historical'):

    folder = '/rds/projects/l/leckebgc-pre-cax/ngks/cop26_bristol/project01/data/raw_data/CMIP6 steric SSH'
    expr = scenario.lower()
    if expr == 'historical':
        mip = "CMIP"
        yr_strt = 1801
        yr_end = 2040
        yr_ref = 2000
    else:
        mip = "ScenarioMIP"
        yr_strt = 2001
        yr_end = 2310
        yr_ref = 2020

    n_mnths = 12 * (yr_end - yr_strt + 1)
    n_ref = 12 * (yr_ref - yr_strt) + 1
    fn = f"{folder}/cmip6_{mip}_{expr}_strh_zostoga_gm.dat"

    fid = open(fn, mode = 'rb')
    a = array.array("i")
    a.fromfile(fid, 1)

    b = a[0]
    n_vals = b // 4
    n_runs = n_vals // n_mnths

    tmp = array.array("f")
    tmp.fromfile(fid, b//4+1)
    tmp = tmp[1:]
    tmp = np.asarray(tmp)
    strh_gm = np.reshape(tmp, (n_runs, n_mnths), 'F')
    strh_gm[strh_gm==0] = np.nan
    for i in range(n_runs): # reference to Jan 2000
      strh_gm[i,:] = strh_gm[i,:] - strh_gm[i,n_ref]

    x = (np.arange(n_mnths) + .5)/12 + yr_strt

    #-----------------------
    modelnames = pd.read_csv(f'{folder}/cmip6_{mip}_{expr}_strh_zostoga_gm_list.txt', sep = '\s+', names=['no','model','run','val1','val2'], index_col='no')

    t = x
    steric = strh_gm
    steric[-1,-1] = np.nan

    #remove fishy first values:
    for no in range(steric.shape[0]):
        ixfirst = np.argmax(~np.isnan(steric[no,:]))
        if np.abs(steric[no,ixfirst]-steric[no,ixfirst+1])>0.1:
            steric[no,ixfirst] = np.nan

    #remove sudden outliers:
    m = median_filter(steric,size=(5,1))
    steric = np.where(np.abs(steric-m)>1, m, steric)

    return (t, steric.T, modelnames)



if __name__ == "__main__":
    # this is some test code:
    t,z,names = load_gm_steric('historical')
    ##print(names)
    nt = len(t)
    for i in range(2,nt):
        print(t[i]-t[i-1])
#        print(str(t[i])+","+str(len(z[i])))
    exit()
    import matplotlib.pyplot as plt
    plt.plot(t,z)
    plt.savefig("test.png")
