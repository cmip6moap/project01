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
        confidence_ellipse(g.Tavg_ice, g.GMSL*1000, facecolor=col, alpha=.3, label=label)
    else:
        confidence_ellipse(g.Tavg_ice, g.GMSL*1000, facecolor=col, alpha=.3)


plot_comparison('GMSL')

plt.title(f'GMSL')
plt.xlabel("Temporal average of GMST (°C)")
plt.ylabel("$dS/dt$ (mm/yr)")
plt.legend(fontsize='small')
plt.show()

