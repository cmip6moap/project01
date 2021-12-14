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
from settings import scenariocolors, baseline_period, datafolder
from misc_tools import confidence_ellipse
from plot_comparison_data import plot_comparison



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
        confidence_ellipse(g.Tavg_ice, g.GMSL*1000, facecolor=col, label=label)
    else:
        confidence_ellipse(g.Tavg_ice, g.GMSL*1000, facecolor=col, linestyle = '--')



#ADD AR6
if True:
    Sar6 = pd.read_csv(f"{datafolder}/raw_data/AR6 Fig spm08ad/global_sea_level_projected.csv",index_col='Year')
    scenarios = ['SSP1-1.9', 'SSP1-2.6', 'SSP2-4.5', 'SSP3-7.0', 'SSP5-8.5']
    tasfile = f"{datafolder}/raw_data/AR6 Fig spm08ad/tas_global_Historical.csv"
    tas =pd.read_csv(tasfile)
    tasbase = tas[(tas.Year>=baseline_period[0]) & (tas.Year<=baseline_period[1])].mean()
    for scenario in scenarios:
        tasfile = f"{datafolder}/raw_data/AR6 Fig spm08ad/tas_global_{scenario.replace('-','_').replace('.','_')}.csv"
        tas =pd.read_csv(tasfile)
        s = Sar6[f'{scenario} Central']
        dSdt = (s[2100]-s[2050])/50
        t = tas[(tas.Year>=2050) & (tas.Year<=2100)].mean() - tasbase
        plt.plot(t['Mean'],dSdt*1000,'bo')
        # dSdt = (s[2050]-s[2020])/30
        # t = tas[(tas.Year>=2020) & (tas.Year<=2050)].mean() - tasbase
        # plt.plot(t['Mean'],dSdt*1000,'mo')
        # dSdt = (s[2100]-s[2020])/70
        # t = tas[(tas.Year>=2020) & (tas.Year<=2100)].mean() - tasbase
        # plt.plot(t['Mean'],dSdt*1000,'ro')

plot_comparison('GMSL')

plt.title(f'GMSL')
plt.xlabel("Temporal average of GMST (°C)")
plt.ylabel("$dS/dt$ (mm/yr)")
plt.legend(fontsize='small')
plt.show()

