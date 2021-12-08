# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 10:05:50 2021

@author: ag
"""

import steric_tools

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from settings import datafolder


def load_trend(scenario):
    t,Z,names = steric_tools.load_gm_steric(scenario)
    names = names.loc[:,['model','run']]
    ix = np.flatnonzero((t>2000) & (t<2027))
    names[f'{scenario}_trend'] = np.nan
    for col in range(Z.shape[1]):
        x = t[ix] - 2000
        y = Z[ix,col]
        nix = np.flatnonzero(~np.isnan(y))
        if len(nix)>12*5:
            p = np.polyfit(x[nix],y[nix],1)
            names.iat[col,-1] = p[0]*1000
    names[f'{scenario}_rowindex'] = range(Z.shape[1])
    names = names.set_index(['model','run'])
    return names


hist = load_trend('historical')
ssp126 = load_trend('ssp126')
ssp245 = load_trend('ssp245')
ssp585 = load_trend('ssp585')


m = pd.concat([hist, ssp126, ssp245, ssp585], axis=1)

m.to_excel(f'{datafolder}/processed_data/debug_mismatch.xls')
