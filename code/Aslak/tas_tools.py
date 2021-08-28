"""

This script contains helper functions for reading the TAS files in
https://github.com/cmip6moap/project01/tree/main/data/raw_data/cmip6_tas_for_steric_analysis

Aslak Grinsted 2021 during CMIP6moap
"""



import numpy as np
import pandas as pd
import re
import os.path
import glob


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
    return r,i,p,f


#---old temperatures---
# def load_tas_knmi(model= 'ACCESS-CM2', scenario='ssp126', run='r1i1p1f1'):
#     folder = '../../data/raw_data/CMIP6_TAS'
#     r,i,p,f = parse_run(run)
#     if scenario == 'historical':
#         scenario = '*'
#         print('warning: am i usng the right one?')
#     r = r.zfill(2)
#     filename = f'{folder}/global_tas_mon_{model}_{scenario}_i{i}p{p}f{f}_{r}.dat'
#     if not os.path.isfile(filename):
#         print(f'file not found: {filename} - trying fallback *_ave')
#         filename = f'{folder}/global_tas_mon_{model}_{scenario}_i{i}p{p}f{f}_ave.dat'
#         filename = glob.glob(filename)[0]
#     df = pd.read_csv(filename, comment='#', sep='\s+', names=['year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'], index_col='year')
#     return df

def load_tas(model= 'ACCESS-CM2', scenario='historical', run='r1i1p1f1_gn', return_annual=True):
    folder = f'../../data/raw_data/cmip6_tas_for_steric_analysis/{scenario}'
    # r,i,p,f = parse_run(run)
    # r = r.zfill(2)
    #gm_tas_CMIP_historical_ACCESS-CM2_r1i1p1f1_gn.csv
    if scenario == 'historical':
        mip = 'CMIP'
    else:
        mip = 'ScenarioMIP'

    filename = f'{folder}/gm_tas_{mip}_{scenario}_{model}_{run}.csv'

    if not os.path.isfile(filename):
        print(f'file not found: {filename}')
        return None
    df = pd.read_csv(filename)
    df['month'] = df.time % 100
    df['year'] = ((df.time-df.month)/100).astype(int)
    if return_annual:
        return df.groupby('year').agg({'gm_tas': 'mean'})
    return df







if __name__ == "__main__":
    # this is some test code:
    d = load_tas()
    import matplotlib.pyplot as plt
    plt.plot(d)