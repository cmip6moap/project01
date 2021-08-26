

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hadcrut5
import steric_tools
import tas_tools
import re



targetperiods = np.array([[1850,1900],[1900,1950],[1950,2000],[1992,2014],[2016,2050],[2051,2100]])


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
            Tbase = np.mean(tas.loc[1995:2014].values)
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


fout = '../../data/processed_data/ExtractedFromSSH/StericTvsRate.csv'
output.to_csv(fout)



scenariocolors = {
    "SSP119": "#e6194B",
    "SSP126": "#3cb44b",
    "SSP245": "#ffe119",
    "SSP370": "#4363d8",
    "SSP585": "#f58231",
    "SSPNDC": "#42d4f4",
    "historical": "#42d4f4"
}


#plt.scatter(output.Tavg, output.dSdt*100, c=output.scenario.map(scenariocolors),s =5)
h= plt.scatter(output.Tavg, output.dSdt*100, c=output.startyr,s =5)
plt.colorbar(h)
G=output.groupby(['scenario','startyr']).agg('median')
plt.scatter(G.Tavg, G.dSdt*100,c= 'k')

plt.xlabel('Temporal average of GMST anomaly (K)')
plt.ylabel('dSSH/dt (m/century)')


# ------------ PLOT comparison data --------------
sheet_name = 'Steric'
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
        c="r",
    )
    plt.text(Trow["Tanom"], row["Rate"] - row["RateSigma"], row["Name"],c='r')
