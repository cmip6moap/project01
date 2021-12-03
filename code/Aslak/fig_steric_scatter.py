

#
# load and plot Tavg-vs-dSdt calculated by extract_steric.py
#
# Aslak Grinsted 2021
#

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hadcrut5
from settings import scenariocolors, datafolder
from misc_tools import confidence_ellipse
from plot_comparison_data import plot_comparison



#fname = f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate.csv'
# fname = f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate_with_weights.csv'
fname = f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate_avg_with_weights.csv'
df = pd.read_csv(fname, index_col=0)


df = df.dropna() # there are some NaNs. Maybe due to incomplete temporal coverage?
#TODO: look into why there are nans!





plt.figure(dpi=300)
G = df.groupby(["scenario", "startyr", "endyr"])
for groupix, g in G:
    scenario = groupix[0]
    col = scenariocolors[scenario.upper()]

    plt.scatter(
        g.Tavg,
        g.dSdt * 1000,
        c=col,
        s=5,
        zorder=-1,
        edgecolors='none',
        alpha=0.4,
    )
    label = f'{scenario}'
    if scenario == 'historical':
        label = f'{groupix[1]}-{groupix[2]}'

    if groupix[1] < 2040:
        confidence_ellipse(g.Tavg, g.dSdt*1000, weights = g.probability_weight, facecolor=col, label=label)
    else:
        confidence_ellipse(g.Tavg, g.dSdt*1000, weights = g.probability_weight, facecolor=col, linestyle='--')
# ------------ PLOT comparison data --------------

sheet_name='Steric'
plot_comparison(sheet_name)
plt.title(f'{sheet_name}')
plt.xlabel("Temporal average of GMST (°C)")
plt.ylabel("$dS/dt$ (mm/yr)")
plt.legend(fontsize='small')
plt.show()


