


import numpy as np
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm




steric = pd.read_csv('../../data/processed_data/ExtractedFromSSH/StericTvsRate.csv')


tfolder = '../../data/processed_data/ExtractedFromTamsin/'
ice = {'WAIS': None,
        'EAIS': None,
        'PEN': None,
        'Glaciers': None,
        'GrIS': None}

risk = False

for tfile in ice:
    fname = f'{tfolder}{tfile}_risk{risk}.csv'
    ice[tfile] = pd.read_csv(fname)





#OUTPUT dataframe
#model

output = pd.DataFrame(
    columns=[
        "model",
        "scenario",
        "startyr",
        "endyr",
        "run",
        "Tavg",
        "run",
        "ice_sample",
        "risk_averse",
        "Steric",
        "WAIS",
        "EAIS",
        "PEN",
        "Glaciers",
        "GrIS",
    ]
)


scenarios = ['SSP126', 'SSP245', 'SSP585']
targetperiods = np.array([[2016,2050],[2051,2100]])

for scenario in scenarios:
    Ssub1 = steric[steric.scenario == scenario]
    for model in tqdm(Ssub1.model.unique()):
        Ssub2 = Ssub1[Ssub1.model == model]
        for periodix in range(targetperiods.shape[0]):
            period = targetperiods[periodix, :]
            #---
            S = Ssub2[(Ssub2.startyr==period[0]) & (Ssub2.endyr==period[1])]
            for ix in range(10):
                s = S.sample().iloc[0]

                Pen = ice['PEN']
                P = Pen[np.abs(s.Tavg - Pen.Tavg)<0.05]
                if len(P)==0:
                    mix = np.argmin(s.Tavg - Pen.Tavg)
                    P = Pen.iloc[mix]
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
                output.loc[output.shape[0]] = newrow #EXTREMELY SLOW!


output['GMSL'] = output['Steric'] + output['GrIS'] + output['Glaciers'] + output['EAIS'] + output['WAIS'] + output['PEN']



df  = output[output.startyr == 2051]
df = output

groups = df.groupby('scenario')
for name, group in groups:
    plt.plot(group["Tavg"], group["GMSL"]*100, marker="o", linestyle="", label=name)
plt.legend()
