




import numpy as np
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import corner
import hadcrut5
import os
from settings import datafolder


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





#OUTPUT dataframe
#model

output = []

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
                output.append(newrow) #EXTREMELY SLOW!

output = pd.DataFrame(output)

output['AIS'] = output['EAIS'] + output['WAIS'] + output['PEN']
output['GMSL'] = output['Steric'] + output['GrIS'] + output['Glaciers'] + output['EAIS'] + output['WAIS'] + output['PEN']





#------------------plot a component------------------



#df  = output[output.startyr == 2051]
df = output
groups = df.groupby('scenario')


components = ['GMSL']

#components= ['GMSL']
for component in components:


    for name, group in groups:
        plt.plot(group["Tavg_ice"], group[component]*1000, marker="o", linestyle="", label=name)
    plt.legend()


    #-----------------plot comparison data

    sheet_name = component
    comparison_data = pd.read_excel(
        "../../data/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx",
        sheet_name=sheet_name,
        skiprows=3,
    )
    for ix, row in comparison_data.iterrows():
        Trow = hadcrut5.getTstats(row["Period start"], row["Period end"])
        plt.errorbar(
            Trow["Tanom"],
            row["Rate"],
            xerr=Trow["sigmaT"],
            yerr=row["RateSigma"],
            c="k",
        )
        plt.text(Trow["Tanom"], row["Rate"] - row["RateSigma"], row["Name"],c='k', rotation=90, fontsize='x-small')

    plt.title(f'd{component}/dt (m/century)')
    plt.xlabel(f'Tavg')

    plt.show()
