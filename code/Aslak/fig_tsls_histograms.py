# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:47:14 2021

@author: ag
"""

from settings import datafolder
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm



tslsfile = f'{datafolder}/processed_data/TSLS_estimates/tsls_ice_emulator.csv'
df = pd.read_csv(tslsfile)

dfobs = pd.read_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_observations.csv',index_col = 'component')

components = df.ice_component.unique()
for component in components:
    subset = df[df.ice_component == component]

    bins = np.linspace(-0.0012, 0.0042, 50)
    for startyr, group in subset.groupby('startyr'):
        if group.shape[0]<2:
            continue

        plt.hist(group.TSLS, bins, alpha=0.5,
                 label=f'{group.startyr.min()}-{group.endyr.max():.0f}')#': {group.TSLS.mean():.4f}±{group.TSLS.std():.4f}')

    if component in dfobs.index:
        subset_obs = dfobs.loc[component]
        x = np.linspace(plt.xlim()[0],plt.xlim()[1],1000)
        y = norm.pdf(x, loc=subset_obs.TSLS, scale=subset_obs.sigmaTSLS)
        y = y*plt.ylim()[1]/np.max(y)
        plt.plot(x, y, 'k', label = f"{subset_obs['period start']:.0f}-{subset_obs['period end']:.0f} obs")


    plt.legend()
    plt.xlabel('TSLS (m/yr/K)')
    plt.title(component)
    plt.show()