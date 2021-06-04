"""
Aslak Grinsted 2021 during CMIP6moap
"""

import numpy as np
import pandas as pd
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
    return r,i,p,f



def load_tas(model= 'ACCESS-CM2', scenario='ssp126', run='r1i1p1f1'):
    folder = '../../data/raw_data/CMIP6_TAS'
    r,i,p,f = parse_run(run)

    if scenario == 'historical':
        1/0
    r = r.zfill(2)
    filename = f'{folder}/global_tas_mon_{model}_{scenario}_i{i}p{p}f{f}_{r}.dat'

    df = pd.read_csv(filename, comment='#', sep='\s+', names=['year','jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'], index_col='year')
    return df








if __name__ == "__main__":
    # this is some test code:
    d = load_tas()
    import matplotlib.pyplot as plt