"""
This is the first step in treating the steric data files.

It pairs the SSH file with the corresponding TAS file and calculates
Tavg and dSdt for the target periods.

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hadcrut5
import steric_tools
import tas_tools
import re

from settings import targetperiods, baseline_period, datafolder


output = []

scenarios = ['historical','SSP126', 'SSP245', 'SSP585']
Tbaselines={}
for scenario in scenarios:


    t,Z,names = steric_tools.load_gm_steric(scenario)

    for col in range(Z.shape[1]):
        z = Z[:,col]
        # try:
        n = names.loc[col+1]
        # except:
        #     continue
        if np.isnan(z).all():
            print(f'ALL NaNs? {n.model} {n.run}')
            continue


        tas = tas_tools.load_tas(model = n.model, scenario = scenario, run = n.run)
        if not isinstance(tas,pd.DataFrame):
            continue

        base_key=f'{n.model},{n.run}'
        if scenario == 'historical':
            Tbase = np.mean(tas.loc[baseline_period[0]:baseline_period[1]].values)
            Tbaselines[base_key] = Tbase
        else:
            if not base_key in Tbaselines:
                base_key = re.sub('r\d+','r1',base_key)
                #base_key = base_key.replace('EC-Earth3,','EC-Earth3-CC,')
                #base_key = base_key.replace('EC-Earth3-Veg-LR,','EC-Earth3-Veg,')
            if not base_key in Tbaselines:
                print(f'SKIPPED: missing historical run for {base_key}')
                continue
            Tbase = Tbaselines[base_key]

        for periodix in range(targetperiods.shape[0]):
            period = targetperiods[periodix,:]
            if (period[0]<t[0]-1/12) | (period[-1]>t[-1]-1/12):
                continue

            #calculate dSdt
            ix = int((period[0]-t[0])*12+.6)
            if np.isnan(z[ix]):
                ix=ix+1 #sometimes the very first sample is missing!
            z1 = np.mean(z[ix:ix+12])

            ix = int((period[1]-t[0])*12+.6)
            if np.isnan(z[ix]):
                ix=ix-1 #sometimes the very last sample may be missing!
            z2 = np.mean(z[ix:ix+12])

            dSdt = (z2-z1) / (period[1]-period[0])

            #calculate
            Tavg = np.mean(tas.loc[period[0]:period[-1]].values) - Tbase

            if np.isnan(Tavg):
                print(f'Tavg is NaN for {n.model} {n.run} {period[0]}-{period[-1]}')
                continue
            if np.isnan(dSdt):
                print(f'dSdt is NaN for {n.model} {n.run} {period[0]}-{period[-1]}')
                continue

            newrow = {
                "model": n.model,
                "run": n.run,
                "scenario": scenario,
                "startyr": period[0],
                "endyr": period[-1],
                "Tavg": Tavg,
                "dSdt": dSdt,
            }

            output.append(newrow)
output = pd.DataFrame(output)

fout = f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate.csv'
output.to_csv(fout)


