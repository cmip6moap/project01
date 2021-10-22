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
from settings import scenariocolors, datafolder
from misc_tools import confidence_ellipse
from plot_comparison_data import plot_comparison



tfolder = f'{datafolder}/processed_data/ExtractedFromTamsin/'
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
            c=col,
            s=3,
            zorder=-1,
            edgecolors='none',
            alpha=0.4,
        )
        if groupix[-1]<2060:
            confidence_ellipse(g.Tavg,g.dSdt*1000,facecolor=col,alpha=.2, label=f'{scenario}')
        else:
            confidence_ellipse(g.Tavg,g.dSdt*1000,facecolor=col,alpha=.2)
    # ------------ PLOT comparison data --------------
    if region:
        sheet_name = region
    else:
        sheet_name = ice_source
    print(sheet_name)
    plot_comparison(sheet_name)
    if risk:
        plt.title(f'{sheet_name}  Risk averse')
    else:
        plt.title(f'{sheet_name}')
    plt.xlabel("Temporal average of GMST (°C)")
    plt.ylabel("$dS/dt$ (mm/yr)")
    plt.legend()
    plt.show()

