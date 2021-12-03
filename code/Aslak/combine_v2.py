




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
from tqdm import tqdm
from steric_tools import parse_run



# This file combines ice with steric.
#
# 1) Combine the dSdt and T estimates from all contributors
# 2) Combine the TSLS estimates of all contributors (NOT DONE YET)

np.random.seed(1337)

#FIRST COMBINE THE dSdt vs T data.

steric = pd.read_csv(f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate_averaged.csv', index_col=0)
steric['model_key'] = steric.model + ':p' + steric['p'].astype(str) + ':' + steric.startyr.astype(str) + ':' + steric.endyr.astype(str) + ':' + steric.scenario
steric['probability_weight'] = 0.0

#---------------------------------

# steric = pd.read_csv(f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate.csv', index_col=0)
# steric = steric.join(parse_run(steric.run))
# steric['model_key'] = steric.model + ':p' + steric['p'] + ':' + steric.startyr.astype(str) + ':' + steric.endyr.astype(str) + ':' + steric.scenario

# mymean = lambda x: x.mean() if x.dtype == np.float64 else x.iloc[0]
# steric = steric.groupby(by=['model_key']).agg(mymean).reset_index()

# steric['probability_weight'] = 0.0

# #Add a column with how many times each model_key appears in the dataset
# counts = steric.pivot_table(index=['model_key'], aggfunc='size')
# counts = pd.DataFrame(counts) # Convert Series to DataFrame
# counts.index.name = 'model_key'
# counts.reset_index(inplace=True) # Change row names to be a column
# counts.columns = ['model_key', 'counts']
# steric = steric.merge(counts) # Merge dataframes on common column



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

    Six = steric.index[(steric.startyr == startyr) &
               (steric.endyr == endyr) &
               (steric.scenario == scenario)]
    S = steric.loc[Six]

    # select a random model based on a probability.
    # The probability of selecting a steric model run depends on
    #  - a similar TAS response. (here we use a normal distribution)

    dT = S.Tavg-irow.Tavg.iloc[0]

    p = norm.pdf(dT.values,0,0.2)
    steric.loc[Six,'probability_weight'] = S.probability_weight + p

    p = np.cumsum(p)/np.sum(p)
    ix = np.flatnonzero(p>=np.random.rand())[0]


    s = S.iloc[ix]
    dT = dT.iloc[ix]


    #The selected model does not have an exact temperature match to the emulator.
    # - so we use the estimated TSLS to adjust for the mismatch in temperature.
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
        "p": s.p,
        #"run": s.run,
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


#
#There are no probability_weight for historical runs.
#Fetch weights from corresponding projection runs.
for index, row in steric.iterrows():
    if row.probability_weight>0:
        continue
    similar = steric[(row.model == steric.model) &
                     (row.p == steric.p) &
                     #(row.r == steric.r) &
                     (steric.endyr>2060) &
                     (steric.scenario == 'SSP585')]
    if len(similar)>0:
        steric.loc[index,'probability_weight'] = similar.probability_weight.sum()

#the above method will give zero weight to model-runs that have not been run for ssp585.


steric.to_csv(f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate_avg_with_weights.csv')

import fig_gmsl_scatter