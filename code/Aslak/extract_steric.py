"""
This is the first step in treating the steric data files.

It pairs the SSH file with the corresponding TAS file and calculates
Tavg and dSdt for the target periods.

Modified by Kelvin Ng 2021 Oct
--> Baseline historical TAS records are now read if steric SSP exist

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hadcrut5
import steric_tools
import tas_tools
import re
from tqdm import tqdm
from steric_tools import parse_run


from settings import targetperiods, baseline_period, datafolder, eflag

output = []

scenarios = ['historical','SSP126', 'SSP245', 'SSP585']
Tbaselines={}
for scenario in scenarios:
    t,Z,names = steric_tools.load_gm_steric(scenario)

    for col in range(Z.shape[1]):
        z = Z[:,col]
        n = names.iloc[col]

    ## SKIP if steric timeseries is full of NaN
        if np.isnan(z).all():
            if eflag == 1:
                print(f'ALL NaNs? {n.model} {n.run}')
            continue
    ## Read TAS data
        tas = tas_tools.load_tas(model = n.model, scenario = scenario, run = n.run)
        if not isinstance(tas,pd.DataFrame):
            if eflag == 1:
                print(f'No {scenario} TAS timeseries {n.model} {n.run}')
            continue

    ## Create key for dictionary
        base_key=f'{n.model},{n.run}'

    ## If it has not been calculated before,
    ## we will calculate historical baseline here if the file exits
        if not base_key in Tbaselines:
            tas_his = tas_tools.load_tas(model = n.model, scenario = "historical", run = n.run)
            if not isinstance(tas_his,pd.DataFrame):
                if eflag == 1:
                    print(f'No Historical TAS timeseries {n.model} {n.run}')
                continue
            Tbase = np.mean(tas_his.loc[baseline_period[0]:baseline_period[1]].values)
            Tbaselines[base_key] = Tbase
    ## Safety check:
    ## If historical baseline has not been calculated at this point,
    ## Such file does not exist, so we skip
        if not base_key in Tbaselines:
            if eflag == 1:
                print(f'SKIPPED: missing historical run for {base_key}')
            continue
    ## Main calculation
        for periodix in range(targetperiods.shape[0]):
            period = targetperiods[periodix,:]
            if (period[0]<t[0]-1/12) | (period[-1]>t[-1]-1/12):
                continue
            #calculate dSdt
            ix = int((period[0]-t[0])*12+.6)    ## Calculate the index closest to period start
    ## Note: Instead of manually skipping element, we can use nanmean to neglect all NaN within the
    ##       period of interest.
            if np.count_nonzero(~np.isnan(z[ix:ix+12])) == 0:
                ## SKIP
                if eflag == 1:
                    print(f'Warning NaN STERIC for {n.model} {n.run} {period[0]} {scenario}')
                continue
            z1 = np.nanmean(z[ix:ix+12])        ## Calculate mean ignoring NAN
            ix = int((period[1]-t[0])*12+.6)
            if np.count_nonzero(~np.isnan(z[ix:ix+12])) == 0:
                ## SKIP
                if eflag == 1:
                     print(f'Warning NaN STERIC for {n.model} {n.run} {period[-1]} {scenario}')
                continue
            z2 = np.nanmean(z[ix:ix+12])        ## Calculate mean ignoring NAN
            dSdt = (z2-z1) / (period[1]-period[0])

            #calculate
            if np.count_nonzero(~np.isnan(tas.loc[period[0]:period[-1]].values)) == 0:
            ## SKIP
                if eflag == 1:
                    print(f'Warning NaN TAS for {n.model} {n.run} {period[0]}-{period[-1]} {scenario}')
                continue
            Tavg = np.nanmean(tas.loc[period[0]:period[-1]].values) - Tbaselines[base_key]

            if np.isnan(Tavg):
                if eflag == 1:
                    print(f'Tavg is NaN for {n.model} {n.run} {period[0]}-{period[-1]} {scenario}')
                continue
            if np.isnan(dSdt):
                if eflag == 1:
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

fout = f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate_individualruns.csv'
output.to_csv(fout)


#save another version where models have been averaged.
steric = output
steric = steric.join(parse_run(steric.run))
steric = steric.groupby(by=['model','p','scenario','startyr','endyr']).agg('mean').reset_index()

fout = f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate_averaged.csv'
steric.to_csv(fout)






