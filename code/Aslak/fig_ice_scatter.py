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
from settings import scenariocolors, datafolder, figurefolder
from misc_tools import confidence_ellipse
from plot_comparison_data import plot_comparison



tfolder = f'{datafolder}/processed_data/ExtractedFromTamsin/'
# components = ['GrIS','WAIS', 'EAIS', 'PEN', 'GIC']
components = ['GrIS','WAIS', 'EAIS', 'GIC']

risk = False

# fig = plt.figure(dpi=300,size=[7,10])
# ax_mosaic = fig.subplot_mosaic([['GrIS','GIC'],['WAIS','EAIS']])



for component in components:
    fname = f'{tfolder}{component}_risk{risk}.csv'
    if not os.path.isfile(fname):
        fname = fname.replace('True','False')
        continue
    # plt.sca(ax_mosaic[component])

    df = pd.read_csv(fname)
    df = df.loc[df.scenario != 'SSPNDC']

    plt.figure(dpi=300)

    ice_source = df.iloc[0].ice_source
    region = df.iloc[0].region
    if not isinstance(region,str):
        region = None
    G = df.groupby(["scenario", "startyr", "endyr"])

    for groupix, g in G:
        scenario = groupix[0]
        col = scenariocolors[scenario]
        #marker = 'P' if (groupix[-1]<2060) else 'o'
        plt.scatter(
            g.Tavg,
            g.dSdt * 1000,
            c=col,
            s=3,
            edgecolor=None,
            zorder=-1,
            alpha=0.2,
        )
        if groupix[-1]<2060:
            confidence_ellipse(g.Tavg,g.dSdt*1000,facecolor=col, label=f'{scenario}')
        else:
            print(g.Tavg.mean())
            confidence_ellipse(g.Tavg,g.dSdt*1000,facecolor=col, linestyle = '--')
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
    plt.savefig(f'{figurefolder}/{sheet_name}_scatter.png',bbox_inches='tight',dpi=600)

    plt.show()

