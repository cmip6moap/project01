# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:35:38 2021

@author: ag
"""


import numpy as np
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import corner
import hadcrut5
import re
from settings import datafolder



comparisonfile = f'{datafolder}/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx'


sheets = ['GMSL', 'Steric', 'Glaciers', 'GrIS', 'AIS', 'WAIS', 'EAIS', 'PEN']

output = []
for sheet in sheets:
    df = pd.read_excel(comparisonfile, sheet, comment="#")
    if len(df)<2:
        print(f'insufficient historical data to estimate TSLS for {sheet}')
        continue
    df['Tanom'] = df.apply(lambda row: hadcrut5.getTstats(row['Period start'],row['Period start'])['Tanom'], axis=1)
    df['sigmaT'] = df.apply(lambda row: hadcrut5.getTstats(row['Period start'],row['Period start'])['sigmaT'], axis=1)

    x = df['Tanom'].values
    y = df['Rate'].values/1000 #m/yr
    sigmax = df['sigmaT'].values
    sigmay = df['RateSigma'].values/1000 #m/yr

    #note this assumes independent errors...
    Nmc = 1000
    slopes = np.full((Nmc),np.nan)
    T0s = np.full((Nmc),np.nan)
    o_intercept = np.full((Nmc),np.nan)
    for ii in range(Nmc):
        p = np.polyfit(x+np.random.randn(x.size)*sigmax,
                       y+np.random.randn(y.size)*sigmay,1,w=1/sigmay)
        slopes[ii] = p[0]
        o_intercept[ii] = p[1]
        T0s[ii] = -p[1] / p[0]

    output.append({
            'component': sheet,
            'period start': df['Period start'].min(),
            'period end': df['Period end'].max(),
            'TSLS': np.mean(slopes),
            'T0': np.mean(T0s),
            'Srate0': np.mean(o_intercept),
            'sigmaTSLS': np.std(slopes),
            'sigmaT0': np.std(T0s),
            'sigmaSrate0': np.std(o_intercept),
        })

output = pd.DataFrame(output)


output.to_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_observations.csv')
