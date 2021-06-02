# -*- coding: utf-8 -*-



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import re
import hadcrut5


distinctcolors = ['#e6194B', '#3cb44b', '#ffe119','#4363d8', '#f58231', '#42d4f4', '#f032e6', '#fabebe', '#469990', '#e6beff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#000075', '#a9a9a9', '#ffffff', '#000000']

ice_source = 'Glaciers'
region = None
risk_averse = False

if risk_averse:
    folder = '../../data/raw_data/Landice-Edwards21/proj_S11_RISK_TIMESERIES'
else:
    folder = '../../data/raw_data/Landice-Edwards21/proj_MAIN_TIMESERIES'



files = glob.glob(folder + '/projections_*.csv')

T2015 = hadcrut5.getTstats(2010,2020)['Tanom']

fileix = 0
for file in files:
    scenario = re.findall('_FAIR_([^\.]*)',file)[0]

    V = pd.read_csv(file);
    V.collapse = V.collapse.fillna(0)
    V = V[V.ice_source == ice_source]

    if region is None:
        #None is intended as a wildcard for all regions. Calculate the sum of all
        V = V.groupby(by=['sample','year']).agg({'SLE': 'sum', 'GSAT': 'mean'}, as_index=False).reset_index()

    Q = V.groupby(by=['sample'])
    Q = Q.agg({'GSAT': 'mean', 'SLE': lambda x: (x.iloc[-5:].mean())*100/(2098-2015)}, as_index=False).reset_index()

    h=plt.scatter(Q.GSAT+T2015, Q.SLE/100, c=distinctcolors[fileix], s=2, alpha=.5)
    plt.scatter(Q.GSAT.median()+T2015, Q.SLE.median()/100, c=distinctcolors[fileix], s=50, zorder=10, edgecolors='k', label=scenario)
    #plt.hist2d(Q.GSAT+0.10,Q.SLE/100, bins=30, cmap='Blues')
    fileix = fileix + 1

#------------ PLOT comparison data --------------
if region is None:
    sheet_name = ice_source
else:
    sheet_name = region

comparison_data = pd.read_excel(
        "../../data/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx",
        sheet_name = sheet_name,
        skiprows = 3,
    )
for ix, row in comparison_data.iterrows():
    Trow = hadcrut5.getTstats(row['Period start'], row['Period end'])
    plt.errorbar(Trow['Tanom'], row['Rate'], xerr = Trow['sigmaT'], yerr = row['RateSigma'], c='k')
    plt.text(Trow['Tanom'], row['Rate'], row['Name'])



plt.xlabel('mean T')
plt.ylabel('SLE_2100')
plt.legend()