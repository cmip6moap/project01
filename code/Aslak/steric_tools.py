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

from functools import lru_cache
import numpy as np
import matplotlib.pyplot as plt
import array
import pandas as pd
#from scipy.ndimage import median_filter  # used for outlier removal
from settings import datafolder
import re

def parse_run(run):
    if isinstance(run, pd.Series):
        return pd.DataFrame(run.map(parse_run).tolist(),index=run.index)
    r = re.findall('(\w)([0-9]+)', run)
    return {e[0]: e[1] for e in r}



def load_gm_steric(scenario = 'historical', apply_drift_correction=False):

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
    #modelnames=modelnames.join(parse_run(modelnames.run))

    t = x
    steric = strh_gm
    steric[-1,-1] = np.nan

#    if scenario=='ssp126':
#        ix = np.where(modelnames.model == 'IPSL-CM5A2-INCA')[0]
#        steric[:,ix] = np.nan
    if apply_drift_correction:
        drift = calc_drift()
        for col in range(len(modelnames)):
            m = modelnames.iloc[col]
            d = drift[(drift.model == m.model) & (drift.p == m.p) & (drift.f == m.f) & (drift.i == m.i)]
            steric[:,col] = steric[:,col] - (t-2000)*d.drift.mean()


    return (t, steric.T, modelnames)


@lru_cache(maxsize=None)
def calc_drift():
    t,Z,names = load_gm_steric('historical', apply_drift_correction=False)
    ix = np.flatnonzero((t>=1958) & (t<2015)) #table 1 https://journals.ametsoc.org/view/journals/clim/31/3/jcli-d-17-0502.1.xml
    drift = np.zeros(Z.shape[1]) + np.nan
    for col in range(len(drift)):
        if np.any(np.isnan(Z[ix,col])):
            continue
        p = np.polyfit(t[ix]-2000,Z[ix,col],1)
        drift[col] = p[0] - 0.54e-3
    names['drift'] = drift
    return names.join(parse_run(names.run))





if __name__ == "__main__":
    ## this is some test code:
    # t,Z,names = load_gm_steric('ssp126',False)
    # import matplotlib.pyplot as plt
    # #plt.plot(t,Z)
    # for col in range(47,52):
    #     z = Z[:,col]
    #     n = names.loc[col+1]
    #     print(str(col),n.model,n.run,n.val1,n.val2)
    #     plt.plot(t,z,label=f'col{col}: {n.model}')
    # plt.legend()


    t,Z,names = load_gm_steric('historical',False)
    col = np.random.randint(0,len(names))
    n = names.iloc[col]
    plt.plot(t,Z[:,col],label=f'historical {n.model} {n.run}')
    plt.title(col)


    t,Z,names = load_gm_steric('ssp245',False)
    col = np.flatnonzero((names.model == n.model) & (names.run == n.run))
    if len(col)>0:
        col=col[0]
        n = names.iloc[col]
        plt.plot(t,Z[:,col],label=f'ssp245 {n.model} {n.run}')

    plt.legend()

    # #-------------TEST drift correciton.
    # t,Z,names = load_gm_steric('ssp245',False)
    # modelnames=names.join(parse_run(names.run))
    # steric=Z
    # plt.plot(t,steric)
    # plt.show()
    # drift = calc_drift()
    # for col in range(len(modelnames)):
    #     m = modelnames.iloc[col]
    #     d = drift[(drift.model == m.model) & (drift.p == m.p) & (drift.f == m.f) & (drift.i == m.i)]

    #     steric[:,col] = steric[:,col] - (t-2000)*d.drift.mean()
    # plt.plot(t,steric)