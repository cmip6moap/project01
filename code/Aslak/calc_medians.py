# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:24:12 2021

@author: ag
"""

import pandas as pd
import numpy as np


scenarios = ['SSP126', 'SSP245', 'SSP585']
components = ['Glaciers_','GrIS_','AIS_WAIS','AIS_EAIS','AIS_PEN','AIS_']
components = ['AIS_PEN','AIS_EAIS']

G_full = None
for component in components:
    f = f'../../data/processed_data/ExtractedFromTamsin/{component}_riskFalse.csv'
    df = pd.read_csv(f)
    df['component'] = component
    G = df.groupby(['component','scenario','startyr','endyr']).agg({'Tavg': 'median', 'dSdt': 'median'})
    G = G.reset_index()

    G_full = pd.concat([G,G_full])

G_full['dSdt']=G_full.dSdt*1000

print(G_full)
1/0

#-----------------EXTRACT STERIC-------------------
df = pd.read_csv('../../data/processed_data/ExtractedFromSSH/StericTvsRate.csv')
#df = df[df['model'].str.contains('^CanESM')]
df.dSdt = df.dSdt*1000

G = df.groupby(['scenario','startyr','endyr']).agg('median').reset_index()
