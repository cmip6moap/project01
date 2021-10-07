# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:47:14 2021

@author: ag
"""

from settings import datafolder, periodcolors
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm



iceemu = pd.read_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_ice_emulator.csv')
steric = pd.read_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_steric.csv')
comparisondata = pd.read_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_observations.csv',index_col = 'component')




ptiles = [5,17,50,83,95] # percentiles of interest.

components = ['Glaciers', 'GrIS', 'WAIS', 'EAIS', 'PEN', 'AIS', 'Land Ice', 'Steric', 'GMSL']


def myboxplot(y, ptilerng, color, rightlabel=''):
    if ptilerng[-1]>plt.xlim()[1]:
        ptilerng[-1]=np.nan
        ptilerng[0]=np.nan
    ybox = np.array([-1,-1,1,1])*.4+y
    plt.plot([ptilerng[0],ptilerng[-1]], [y,y],color = color,linewidth=2,clip_on = False)
    plt.fill([ptilerng[1],ptilerng[3],ptilerng[3],ptilerng[1]],
             ybox, color = color,clip_on = False)
    plt.plot(ptilerng[2]+np.zeros(2),ybox[1:3],'k',alpha=0.5,clip_on = False)
    plt.text(np.nanmax(ptilerng),y,f' {rightlabel}',
             fontsize='x-small',alpha = 0.5,verticalalignment='center',clip_on = False)


fig1 = plt.figure(figsize = [5,5], facecolor='white', dpi=300)
plt.gca().set_frame_on(False)
plt.gca().axes.get_yaxis().set_visible(False)
plt.xlim([-.5, 8])

yrow = 0
for component in components:
    yrow = yrow + 1.5
    ystart = yrow
    if component in iceemu.ice_component.unique():
        subset = iceemu[iceemu.ice_component == component]
    elif component == 'Steric':
        subset = steric
    else:
        if component == 'AIS':
            subset = iceemu[iceemu.ice_component.isin(['EAIS','WAIS','PEN'])]
        elif component in ['Land Ice', 'GMSL']:
            subset = iceemu
        else:
            continue
        g = subset.groupby(['model_key','startyr','endyr'], as_index = False)
        subset = g.agg({'TSLS': np.sum})
        if component == 'GMSL':
            #at this point subset is land_ice - now add steric
            for index, row in subset.iterrows():
                s = steric[(steric.startyr == row.startyr) & (steric.endyr == row.endyr)]
                stericTSLS = s.TSLS.sample(1).values
                subset.at[index,'TSLS'] = subset.at[index,'TSLS'] + stericTSLS



    for startyr, group in subset.groupby('startyr'):
        if group.shape[0]<2:
            continue
        ps = np.percentile(group.TSLS*1000,ptiles)
        lbl = f'{group.startyr.iloc[0]}-{group.endyr.iloc[0]}'
        col = periodcolors[lbl]

        myboxplot(yrow,ps,color=col,rightlabel=lbl)
        yend = yrow
        yrow = yrow + 1



    if component in comparisondata.index:
        subset_obs = comparisondata.loc[component]
        mu = subset_obs.TSLS*1000
        sigma = subset_obs.sigmaTSLS*1000
        ps= [np.nan, mu-sigma*.954, mu, mu+sigma*.954, np.nan]
        lbl = f"{subset_obs['period start']:.0f}-{subset_obs['period end']:.0f}"
        myboxplot(yrow,ps,'#888888',lbl)
        yend = yrow
        yrow = yrow + 1



    plt.text(-.7,(yend+ystart)/2,component,horizontalalignment='right',verticalalignment='center')

        # x = np.linspace(plt.xlim()[0],plt.xlim()[1],1000)
        # y = norm.pdf(x, loc=subset_obs.TSLS*1000, scale=subset_obs.sigmaTSLS*1000)
        # y = y*plt.ylim()[1]/np.max(y)
        # plt.plot(x, y, 'k', label = f"{subset_obs['period start']:.0f}-{subset_obs['period end']:.0f} obs")


plt.grid(axis='x')
plt.xlabel('TSLS (mm/yr/K)')
plt.show()


#