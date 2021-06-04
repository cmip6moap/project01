

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hadcrut5
import steric_tools
import tas_tools



targetperiods = np.array([[2016,2050],[2050,2100]])


output = pd.DataFrame(
    columns=[
        "model",
        "run",
        "scenario",
        "startyr",
        "endyr",
        "Tavg",
        "dSdt",
    ]
)

scenarios = ['SSP126', 'SSP245', 'SSP585']
for scenario in scenarios:


    t,Z,names = steric_tools.load_gm_steric(scenario)



    for col in range(Z.shape[1]):
        z = Z[:,col]
        n = names.iloc[col]

        try:
            tas = tas_tools.load_tas(model = n.model, scenario = scenario, run = n.run)
        except:
            print(f'MISSING\n{n}\n')
            continue
        Tbase = np.mean(tas.loc[1995:2014].values)

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

            dSdt = (z2-z1)/(period[1]-period[0])

            #calculate
            Tavg = np.mean(tas.loc[period[0]:period[-1]].values) - Tbase

            newrow = {
                "model": n.model,
                "run": n.run,
                "scenario": scenario,
                "startyr": period[0],
                "endyr": period[-1],
                "Tavg": Tavg,
                "dSdt": dSdt,
            }
            output.loc[output.shape[0]] = newrow


scenariocolors = {
    "SSP119": "#e6194B",
    "SSP126": "#3cb44b",
    "SSP245": "#ffe119",
    "SSP370": "#4363d8",
    "SSP585": "#f58231",
    "SSPNDC": "#42d4f4",
}


plt.scatter(output.Tavg, output.dSdt*100, c=output.scenario.map(scenariocolors))
plt.xlabel('Tmean')
plt.ylabel('dSSH/dt (m/century)')
