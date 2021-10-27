"""
This script has helper functions for reading the SSH files here:
    https://github.com/cmip6moap/project01/tree/main/data/raw_data/CMIP6%20steric%20SSH


Based on Rory Binghams example code.


Modified by Aslak Grinsted 2021

Modified by Kelvin Ng 2021 Oct

"""

#
# This is the code that can read the SSH files...
#
#
#

import numpy as np
import matplotlib.pyplot as plt
import array
import pandas as pd
#from scipy.ndimage import median_filter  # used for outlier removal
from settings import datafolder
import re

def parse_run(run):
    r = re.findall('r(\d+|ave)', run)
    if r is None:
        r = re.findall(r'_(\d+|ave)$', run)
    if r:
        r = r[0][0]
    else:
        r = 'ave'
    i = re.findall(r'i(\d+)', run)[0][0]
    p = re.findall(r'p(\d+)', run)[0][0]
    f = re.findall(r'f(\d+)', run)[0][0]
    return {'r': r, 'i': i, 'p': p, 'f': f}



def load_gm_steric(scenario = 'historical'):

    folder = f'{datafolder}/raw_data/CMIP6 steric SSH'
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
    strh_gm[strh_gm<-1.7e7] = np.nan
    for i in range(n_runs): # reference to Jan 2000
      strh_gm[i,:] = strh_gm[i,:] - strh_gm[i,n_ref]

    x = (np.arange(n_mnths) + .5)/12 + yr_strt

    #-----------------------
    modelnames = pd.read_csv(f'{folder}/cmip6_{mip}_{expr}_strh_zostoga_gm_list.txt', sep = '\s+', names=['no','model','run','val1','val2'], index_col='no')

    t = x
    steric = strh_gm
    steric[-1,-1] = np.nan

    return (t, steric.T, modelnames)



if __name__ == "__main__":
    # this is some test code:
    t,z,names = load_gm_steric('historical')
    import matplotlib.pyplot as plt
    plt.plot(t,z)
