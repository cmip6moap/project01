




import numpy as np
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import corner
import hadcrut5
import re
import os
from scipy.stats import norm
from settings import datafolder
from steric_tools import parse_run


# This file combines ice with steric.
#
# 1) Combine the dSdt and T estimates from all contributors
# 2) Combine the TSLS estimates of all contributors



#FIRST COMBINE THE dSdt vs T data.

steric = pd.read_csv(f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate.csv')
steric = steric.join(parse_run(steric.run))
steric['model_key'] = steric.model + ':p' + steric['i'] + ':' + steric.startyr.astype(str) + ':' + steric.endyr.astype(str) + ':' + steric.scenario

counts = steric.pivot_table(index=['model_key'], aggfunc='size')
counts = pd.DataFrame(counts) # Convert Series to DataFrame
counts.index.name = 'model_key'
counts.reset_index(inplace=True) # Change row names to be a column
counts.columns = ['model_key', 'counts']
steric = steric.merge(counts) # Merge dataframes on common column
#---------------------------------

tfolder = f'{datafolder}/processed_data/ExtractedFromTamsin/'
ice = {'WAIS': None,
        'EAIS': None,
        'PEN': None,
        'Glaciers': None,
        'GrIS': None}

tsls_steric = pd.read_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_steric.csv')

risk = False

for tfile in ice:
    fname = f'{tfolder}{tfile}_risk{risk}.csv'
    if not os.path.isfile(fname):
        fname = fname.replace('True','False')
    ice[tfile] = pd.read_csv(fname)

ice = pd.concat(ice,ignore_index=True)

#------------------------------------------------

scenarios = ['SSP126', 'SSP245', 'SSP585']
ice = ice[ice['scenario'].isin(scenarios)]


targetperiods = np.array([[2016,2050],[2051,2100]])

output = []

grouped_ice = ice.groupby(by=['sample','scenario','startyr','endyr'])
for (sample,scenario,startyr,endyr),irow in tqdm(grouped_ice):

    S = steric[(steric.startyr == startyr) &
               (steric.endyr == endyr) &
               (steric.scenario == scenario)]


    dT = S.Tavg-irow.Tavg.iloc[0]

    p = norm.pdf(dT.values,0,0.2) / S.counts.values
    p = np.cumsum(p)/np.sum(p)
    ix = np.flatnonzero(p>=np.random.rand())[0]

    s = S.iloc[ix]
    dT = dT.iloc[ix]

    no_scen_key = re.sub(':[^:]+$','',s.model_key)
    tsls = tsls_steric.TSLS[tsls_steric.model_key==no_scen_key ]
    if len(tsls)>0:
        tsls = tsls.iloc[0]
    else:
        tsls = tsls_steric.TSLS.sample().iloc[0]



    f = irow.iloc[0]
    newrow = {
        "model": s.model,
        "scenario": scenario,
        "startyr": startyr,
        "endyr": endyr,
        "Tavg": s.Tavg, #----------
        "Tavg_ice": f.Tavg,
        "run": s.run,
        "ice_sample": sample,
        "risk_averse": risk,
        "Steric": s.dSdt + dT*tsls,
        "WAIS": irow[irow.region == 'WAIS'].iloc[0].dSdt,  #NOTE THIS ASSUMES matching order between files!!!!
        "EAIS": irow[irow.region == 'EAIS'].iloc[0].dSdt,
        "PEN": irow[irow.region == 'PEN'].iloc[0].dSdt,
        "Glaciers": irow[irow.ice_source == 'Glaciers'].iloc[0].dSdt,
        "GrIS": irow[irow.ice_source == 'GrIS'].iloc[0].dSdt
    }
    output.append(newrow)

output = pd.DataFrame(output)

output['AIS'] = output['EAIS'] + output['WAIS'] + output['PEN']
output['GMSL'] = output['Steric'] + output['GrIS'] + output['Glaciers'] + output['EAIS'] + output['WAIS'] + output['PEN']

fname = f'{datafolder}/processed_Data/combined/combined_dSdt_T.csv'

output.to_csv(fname)


import fig_gmsl_scatter