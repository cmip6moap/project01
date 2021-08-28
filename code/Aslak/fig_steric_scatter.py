

#
# load and plot Tavg-vs-dSdt calculated by extract_steric.py
#
# Aslak Grinsted 2021
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hadcrut5
from settings import scenariocolors
from misc_tools import confidence_ellipse


df = pd.read_csv('../../data/processed_data/ExtractedFromSSH/StericTvsRate.csv')
df = df.dropna() # there are some NaNs. Maybe due to incomplete temporal coverage?
#TODO: look into why there are nans!


G = df.groupby(["scenario", "startyr", "endyr"])
for groupix, g in G:
    scenario = groupix[0]
    col = scenariocolors[scenario.upper()]

    plt.scatter(
        g.Tavg,
        g.dSdt * 100,
        c=col,
        s=4,
        zorder=-1,
        edgecolors='none',
        alpha=0.4,
    )
    label = f'{scenario}'
    if scenario == 'historical':
        label = f'{groupix[1]}-{groupix[2]}'

    if groupix[1]<2040:
        confidence_ellipse(g.Tavg,g.dSdt*100,facecolor=col,alpha=.3, label=label)
    else:
        confidence_ellipse(g.Tavg,g.dSdt*100,facecolor=col,alpha=.3)
# ------------ PLOT comparison data --------------

sheet_name='Steric'
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
    plt.text(Trow["Tanom"], row["Rate"] - row["RateSigma"], row["Name"])

plt.title(f'{sheet_name}')
plt.xlabel("mean T")
plt.ylabel("dSdt (m/century)")
plt.legend()
plt.show()


