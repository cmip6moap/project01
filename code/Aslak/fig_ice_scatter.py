# -*- coding: utf-8 -*-

#
# load and plot Tavg-vs-dSdt calculated by extract_iceemu.py
#
# Aslak Grinsted 2021
#


import numpy as np
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import corner
import hadcrut5
import re
import os
from settings import scenariocolors
from misc_tools import confidence_ellipse




tfolder = '../../data/processed_data/ExtractedFromTamsin/'
components = ['WAIS', 'EAIS', 'PEN', 'Glaciers', 'GrIS']

risk = False

for component in components:
    fname = f'{tfolder}{component}_risk{risk}.csv'
    if not os.path.isfile(fname):
        fname = fname.replace('True','False')
        continue

    df = pd.read_csv(fname)

    plt.figure(dpi=300)

    ice_source = df.iloc[0].ice_source
    region = df.iloc[0].region
    if not isinstance(region,str):
        region = None
    G = df.groupby(["scenario", "startyr", "endyr"])
    for groupix, g in G:
        scenario = groupix[0]
        col = scenariocolors[scenario]
        plt.scatter(
            g.Tavg,
            g.dSdt * 1000,
            c='k',
            s=2,
            zorder=-1,
            edgecolors='none',
            alpha=0.4,
        )
        if groupix[-1]<2060:
            confidence_ellipse(g.Tavg,g.dSdt*1000,facecolor=col,alpha=.3, label=f'{scenario}')
        else:
            confidence_ellipse(g.Tavg,g.dSdt*1000,facecolor=col,alpha=.3)
    # ------------ PLOT comparison data --------------
    if region:
        sheet_name = region
    else:
        sheet_name = ice_source
    print(sheet_name)
    comparison_data = pd.read_excel(
        "../../data/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx",
        sheet_name=sheet_name, comment='#'
    )
    for ix, row in comparison_data.iterrows():
        Trow = hadcrut5.getTstats(row["Period start"], row["Period end"])
        plt.errorbar(
            Trow["Tanom"],
            row["Rate"],
            xerr=Trow["sigmaT"],
            yerr=row["RateSigma"],
            marker = '.', markersize=10,
            c="k",
        )
        plt.text(Trow["Tanom"], row["Rate"] + row["RateSigma"], f' {row["Name"]}',alpha=.6,rotation=90,horizontalalignment='center',verticalalignment='bottom',fontsize=8)

    if risk:
        plt.title(f'{sheet_name}  Risk averse')
    else:
        plt.title(f'{sheet_name}')
    plt.xlabel("Temporal average of GMST (°C)")
    plt.ylabel("$dS/dt$ (mm/yr)")
    plt.legend()
    plt.show()

