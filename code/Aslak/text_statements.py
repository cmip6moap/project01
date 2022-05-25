# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 09:59:44 2021

@author: ag
"""


import pandas as pd
from settings import baseline_period, datafolder

rangefun = lambda x: [x.min(), x.max()]


final = pd.read_csv(f'{datafolder}/processed_data/TSLS_estimates/final_tsls_ranges.csv')
tsls_observations = pd.read_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_observations.csv',index_col='component')

for ix,f in final.iterrows():
    print(f'TSLS {f.component: >11}\t{f.label: >12}\t{f.period}\t{f.p50:.2f} [{f.p5:.2f}–{f.p95:.2f}] mm/yr/K')

print('========MU SIGMA=======')
for ix,f in final.iterrows():
    #if f.period == '2016-2050':
   #     continue
    print(f'{f.component: >11}\t{f.label: >12}\t{f.period}\t{f.mu:.1f}±{f.sigma:.1f} mm/yr/K')



# STERIC SECTION:
print('===========STERIC============')

print(f"Steric observational T0: {tsls_observations.loc['Steric'].T0:.1f}±{tsls_observations.loc['Steric'].sigmaT0:.1f}")

df = pd.read_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_steric.csv')
for startyr in [1850,2016,2051]:
    d = df[df.startyr==startyr]
    endyr = d.iloc[0].endyr
    print(f'models Steric_TSLS range {startyr}–{endyr}: {d.TSLS.min()*1000:.1f}–{d.TSLS.max()*1000:.1f} mm/yr/K')
    print(f'models Steric   T0 range {startyr}–{endyr}: {d.BalanceT.min():.1f}–{d.BalanceT.max():.1f} K')





#=================

tasfile = f"{datafolder}/raw_data/AR6 Fig spm08ad/tas_global_Historical.csv"
tas =pd.read_csv(tasfile)
scenario = 'SSP5-8.5'
tasfile = f"{datafolder}/raw_data/AR6 Fig spm08ad/tas_global_{scenario.replace('-','_').replace('.','_')}.csv"
tasproj = pd.read_csv(tasfile)
tas = pd.concat([tas,tasproj])
tasbase = tas[(tas.Year>=baseline_period[0]) & (tas.Year<=baseline_period[1])].mean()

T21C = tas[tas.Year>=2000].Mean.mean() - tasbase.Mean
T2100 = tas[tas.Year>=2099].Mean.mean() - tasbase.Mean
