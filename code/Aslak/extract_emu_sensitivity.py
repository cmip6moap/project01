# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 09:02:15 2021

@author: ag
"""

# -*- coding: utf-8 -*-


import numpy as np
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import corner
import hadcrut5
import re
import os



tfolder = '../../data/processed_data/ExtractedFromTamsin/'
ice = {'WAIS': None,
        'EAIS': None,
        'PEN': None,
        'Glaciers': None,
        'GrIS': None}

risk = False

for tfile in ice:
     fname = f'{tfolder}{tfile}_risk{risk}.csv'
     if not os.path.isfile(fname):
         fname = fname.replace('True','False')
     ice[tfile] = pd.read_csv(fname)



output = pd.DataFrame(
    columns=[
        "ice_component",
        "model_key",
        "startyr",
        "endyr",
        "Tmin",
        "Tmax",
        "Npts",
        "TSLS",
        "BalanceT",
        "Intercept"
    ]
)


for tfile in ice:
    for key,group in ice[tfile].groupby(['sample','startyr','endyr']):
        sample = key[0]
        startyr = key[1]
        endyr = key[2]
        N = group.shape[1]
        if N<2:
            continue
        p = np.polyfit(group.Tavg.values,group.dSdt.values,1)
        newrow= {
            "ice_component": tfile,
            "model_key": f'sample{sample}',
            "startyr": startyr,
            "endyr": endyr,
            "Tmin": group.Tavg.min(),
            "Tmax": group.Tavg.max(),
            "Npts": N,
            "TSLS": p[0],
            "BalanceT": -p[1]/p[0],
            "Intercept": p[1]
            }
        output.loc[output.shape[0]] = newrow #EXTREMELY SLOW!


df=output[output.ice_component=='EAIS']
for startyr, group in df.groupby('startyr'):
    bins = np.linspace(-0.005, 0.005, 50)
    #bins = np.linspace(-1, 1, 20)
    if group.shape[0]<2:
        continue
    plt.hist(group.TSLS, bins, alpha=0.5, label=f'{group.startyr.min()}-{group.endyr.max()}')
plt.legend()

