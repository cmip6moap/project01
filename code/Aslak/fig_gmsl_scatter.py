# -*- coding: utf-8 -*-

import numpy as np
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import corner
import hadcrut5
import re
import os
from settings import scenariocolors, datafolder
from misc_tools import confidence_ellipse




fname = f'{datafolder}/processed_Data/combined/combined_dSdt_T.csv'
df = pd.read_csv(fname)


plt.figure(dpi=300)
G = df.groupby(["scenario", "startyr", "endyr"])
for groupix, g in G:
    scenario = groupix[0]
    col = scenariocolors[scenario.upper()]

    plt.scatter(
        g.Tavg_ice,
        g.GMSL * 1000,
        c=col,
        s=3,
        zorder=-1,
        edgecolors='none',
        alpha=0.4,
    )
    label = f'{scenario}'
    if scenario == 'historical':
        label = f'{groupix[1]}-{groupix[2]}'

    if groupix[1] < 2040:
        confidence_ellipse(g.Tavg_ice, g.GMSL*1000, facecolor=col, alpha=.3, label=label)
    else:
        confidence_ellipse(g.Tavg_ice, g.GMSL*1000, facecolor=col, alpha=.3)


sheet_name='GMSL'
comparison_data = pd.read_excel(
    f"{datafolder}/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx",
    sheet_name=sheet_name, comment="#"
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
    plt.text(Trow["Tanom"], row["Rate"] + row["RateSigma"], f' {row["Name"]}',alpha=.6,rotation=90,horizontalalignment='center',verticalalignment='bottom',fontsize=8)

plt.title(f'{sheet_name}')
plt.xlabel("Temporal average of GMST (°C)")
plt.ylabel("$dS/dt$ (mm/yr)")
plt.legend(fontsize='small')
plt.show()

