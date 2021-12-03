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
from steric_tools import parse_run
from settings import datafolder



steric = pd.read_csv(f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate_individualruns.csv')
steric['setup'] = steric.run.apply(parse_run)
steric = steric[steric.dSdt.notna()]
steric = steric[steric.Tavg.notna()]

steric_projections = steric[steric.scenario != 'historical']
steric_historical = steric[steric.scenario == 'historical']

output = []

def group_id(row):
    if row.scenario == 'historical':
        return f"{row.model}:p{row.setup['p']}f{row.setup['f']}:historical"
    else:
        return f"{row.model}:p{row.setup['p']}:{row.startyr}:{row.endyr}"

steric['group_id']=steric.apply(group_id,axis=1)

groups = steric.groupby('group_id')
for name, group in groups:
    N = group.Tavg.values.shape[0]
    if N<3:
        continue
    # if (group.Tavg.max()-group.Tavg.min())<0.2:
    #     continue
    p,covp = np.polyfit(group.Tavg.values,group.dSdt.values,1, cov=True)
    newrow= {"model_key": name,
        "startyr": group.startyr.min(),
        "endyr": group.endyr.max(),
        "Tmin":group.Tavg.min(),
        "Tmax":group.Tavg.max(),
        "Npts": N,
        "TSLS": p[0],
        "sigmaTSLS": np.sqrt(covp[0,0]),
        "BalanceT": -p[1]/p[0],
        "Intercept": p[1]
        }
    output.append(newrow)

output = pd.DataFrame(output)

#discard poorly constrained rows. sigmaTSLS
output = output.loc[output.sigmaTSLS < 0.003]


fout = f'{datafolder}/processed_data/TSLS_estimates/tsls_steric.csv'
output.to_csv(fout)


df = output[output['startyr']==1850]
#r = np.random.randn(len(df))
#plt.errorbar(df['Npts']+r*0.1, df['TSLS'], fmt='.', yerr=df['sigmaTSLS'], alpha=0.3)
plt.scatter(df['TSLS']*1000,df['Intercept']*1000,c=df['Npts'],marker='o',alpha=0.7)
s = df[output.model_key.apply(lambda s: s.startswith('FGOALS-f3-L'))]
plt.plot(s['TSLS']*1000,s['Intercept']*1000,'ro')
plt.text(s['TSLS']*1000,s['Intercept']*1000,'FGOALS-f3-L',color='r')
plt.xlabel('TSLS (mm/yr/K)')
plt.ylabel('Intercept (mm/yr)')
plt.title('1850-2014')

# for startyr, group in output.groupby('startyr'):
#     bins = np.linspace(-0.005, 0.005, 20)
#     #bins = np.linspace(-1, 1, 20)
#     if group.shape[0]<2:
#         continue
#     plt.hist(group.TSLS, bins, alpha=0.5, label=f'{group.startyr.min()}-{group.endyr.max()}')
# plt.legend()
# plt.xlabel('TSLS (m/yr/K)')
# plt.title('Steric')

