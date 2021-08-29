# -*- coding: utf-8 -*-
"""
this is step 2 in the steric anaysis.


This groups all the dSdt vs Tavg values by "model",
and makes a regression for each in order to obtain
the steric sensitivity to warming.

This is done for each target period.
The historical period is treated somewhat differently because there are not mulitple scenarios for the historical.


"""

import numpy as np
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import corner
import hadcrut5
import re



steric = pd.read_csv('../../data/processed_data/ExtractedFromSSH/StericTvsRate.csv')
steric['setup'] = steric.run.apply(lambda s: re.findall(r'r\d+i\d+(p\d+)',s)[0])
steric = steric[steric.dSdt.notna()]
steric = steric[steric.Tavg.notna()]

steric_projections = steric[steric.scenario != 'historical']
steric_historical = steric[steric.scenario == 'historical']

output = pd.DataFrame(
    columns=[
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

def group_id(row):
    if row.scenario == 'historical':
        return f'{row.model}:{row.setup}:historical'
    else:
        return f'{row.model}:{row.setup}:{row.startyr}:{row.endyr}'

steric['group_id']=steric.apply(group_id,axis=1)

groups = steric.groupby('group_id')
for name, group in groups:
    N = group.Tavg.values.shape[0]
    if N<2:
        continue
    if (group.Tavg.max()-group.Tavg.min())<0.2:
        continue
    p = np.polyfit(group.Tavg.values,group.dSdt.values,1)
    newrow= {"model_key": name,
        "startyr": group.startyr.min(),
        "endyr": group.endyr.max(),
        "Tmin":group.Tavg.min(),
        "Tmax":group.Tavg.max(),
        "Npts": N,
        "TSLS": p[0],
        "BalanceT": -p[1]/p[0],
        "Intercept": p[1]
        }
    output.loc[output.shape[0]] = newrow #EXTREMELY SLOW!




fout = '../../data/processed_data/TSLS_estimates/tsls_steric.csv'
output.to_csv(fout)





for startyr, group in output.groupby('startyr'):
    bins = np.linspace(-0.005, 0.005, 20)
    #bins = np.linspace(-1, 1, 20)
    if group.shape[0]<2:
        continue
    plt.hist(group.TSLS, bins, alpha=0.5, label=f'{group.startyr.min()}-{group.endyr.max()}')
plt.legend()
plt.xlabel('TSLS (m/yr/K)')
plt.title('Steric')

