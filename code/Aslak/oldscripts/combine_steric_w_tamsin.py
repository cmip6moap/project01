




import numpy as np
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import corner
import hadcrut5
import os
from settings import datafolder


# This file combines ice with steric.
#
# 1) Combine the dSdt and T estimates from all contributors
# 2) Combine the TSLS estimates of all contributors



#FIRST COMBINE THE dSdt vs T data.

steric = pd.read_csv(f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate.csv')

tfolder = f'{datafolder}/processed_data/ExtractedFromTamsin/'
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


output = []

scenarios = ['SSP126', 'SSP245', 'SSP585']
targetperiods = np.array([[2016,2050],[2051,2100]])

for model in tqdm(steric.model.unique()):
    s_model = steric[steric.model == model]
    for periodix in range(targetperiods.shape[0]):
        period = targetperiods[periodix, :]
        s_model_period = s_model[(s_model.startyr==period[0]) & (s_model.endyr==period[1])]
        if len(s_model_period)==0:
            continue
        for scenario in scenarios:
            S = s_model_period[s_model_period.scenario == scenario]
            if len(S)==0:
                continue
            for ix in range(10):
                s = S.sample().iloc[0]

                Pen = ice['PEN']
                Pen = Pen[Pen['scenario'] == scenario]
                P = Pen[np.abs(s.Tavg - Pen.Tavg)<0.1]
                if len(P)==0:
                    mix = np.argmin(s.Tavg - Pen.Tavg)
                    p = Pen.iloc[mix]
                else:
                    p = P.sample().iloc[0]
                newrow = {
                    "model": model,
                    "scenario": scenario,
                    "startyr": period[0],
                    "endyr": period[1],
                    "Tavg": s.Tavg,
                    "Tavg_ice": p.Tavg,
                    "run": s.run,
                    "ice_sample": p['sample'],
                    "risk_averse": risk,
                    "Steric": s.dSdt,
                    "WAIS": ice['WAIS'].loc[p.name].dSdt,  #NOTE THIS ASSUMES matching order between files!!!!
                    "EAIS": ice['EAIS'].loc[p.name].dSdt,
                    "PEN": p.dSdt,
                    "Glaciers": ice['Glaciers'].loc[p.name].dSdt,
                    "GrIS": ice['GrIS'].loc[p.name].dSdt
                }
                output.append(newrow)

output = pd.DataFrame(output)

output['AIS'] = output['EAIS'] + output['WAIS'] + output['PEN']
output['GMSL'] = output['Steric'] + output['GrIS'] + output['Glaciers'] + output['EAIS'] + output['WAIS'] + output['PEN']

fname = f'{datafolder}/processed_Data/combined/combined_dSdt_T.csv'

output.to_csv(fname)

