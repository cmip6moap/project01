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


sheets = ['GMSL', 'Steric', 'GIC', 'GrIS', 'AIS', 'WAIS', 'EAIS', 'PEN', 'All but GIC']

output = []
for sheet in sheets:
    df = pd.read_excel(comparisonfile, sheet, comment="#")
    if len(df)<2:
        print(f'insufficient historical data to estimate TSLS for {sheet}')
        continue
    df['Tanom'] = df.apply(lambda row: hadcrut5.getTstats(row['Period start'],row['Period start'])['Tanom'], axis=1)
    df['sigmaT'] = df.apply(lambda row: hadcrut5.getTstats(row['Period start'],row['Period start'])['sigmaT'], axis=1)

    for min_year in (1000,):#,1990):
        ix = df['Period start']>min_year
        subset = df[ix]

        x = subset['Tanom'].values
        y = subset['Rate'].values/1000 #m/yr
        sigmax = subset['sigmaT'].values
        sigmay = subset['RateSigma'].values/1000 #m/yr

        if (sheet=='GrIS') or (sheet=='AIS'):
            ix = df['Period start']>1990
            p = np.polyfit(x[ix],y[ix],1,w=1/sigmay[ix])
            print(f'{sheet} observational TSLS post 1990: {p[0]*1000:.2f}')

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
        mc = pd.DataFrame()

        ptiles = np.percentile(slopes,[5,17,50,83,95])

        output.append({
                'component': sheet,
                'period start': subset['Period start'].min(),
                'period end': subset['Period end'].max(),
                'TSLS': np.mean(slopes),
                'T0': np.mean(T0s),
                'Srate0': np.mean(o_intercept),
                'sigmaTSLS': np.std(slopes),
                'TSLS_P5': ptiles[0],
                'TSLS_P17': ptiles[1],
                'TSLS_P50': ptiles[2],
                'TSLS_P83': ptiles[3],
                'TSLS_P95': ptiles[4],
                'sigmaT0': np.std(T0s),
                'sigmaSrate0': np.std(o_intercept),
            })

output = pd.DataFrame(output)


output.to_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_observations.csv')

# plt.errorbar(x,y,xerr=sigmax,yerr=sigmay)
# plt.title(sheet)