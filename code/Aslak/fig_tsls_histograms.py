# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:47:14 2021

@author: ag
"""

from settings import datafolder, periodcolors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects


iceemu = pd.read_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_ice_emulator.csv')
steric = pd.read_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_steric.csv')
comparisondata = pd.read_csv(f'{datafolder}/processed_data/TSLS_estimates/tsls_observations.csv',index_col = 'component')

#should some other script derive tsls?
experts = pd.read_excel(f'{datafolder}/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx',sheet_name="Expert", comment="#")


#also save every plotted range as table ... todo
output=[]


ptiles = [5,17,50,83,95] # percentiles of interest.

components = ['GIC', 'GrIS', 'WAIS', 'EAIS', 'PEN', 'AIS', 'Land Ice', 'Steric', 'All but GIC', 'GMSL']


def myboxplot(y, ptilerng, name, component='', rightlabel='', islabel = False):
    mx = plt.xlim()[1]
    if name in periodcolors:
        color = periodcolors[name]
    elif rightlabel in periodcolors:
        color = periodcolors[rightlabel]
    else:
        color = name
    newrow = {
            "component": component,
            "label": name,
            "period": rightlabel,
            "p5": ptilerng[0],
            "p17": ptilerng[1],
            "p50": ptilerng[2],
            "p83": ptilerng[3],
            "p95": ptilerng[4],
    }


    if ptilerng[-1] > mx:
        plt.plot([ptilerng[0],ptilerng[3]],[y,y],color = color,linewidth=2,clip_on = False,alpha=0.4)
        plt.arrow(ptilerng[3],y,mx-ptilerng[3],0,
                  head_length=0.1,head_width=0.2,
                  length_includes_head=True,
                  color=color,
                  linewidth=2,clip_on = False,alpha=0.4)
        # plt.text(mx,y,f' {ptilerng[-1]:.0f}',
        #      fontsize='xx-small',alpha = 0.7,
        #      horizontalalignment = 'left',
        #      color=color,
        #      verticalalignment='center',clip_on = False)
        ptilerng[-1]=np.nan
        ptilerng[0]=np.nan
    else:
        plt.plot([ptilerng[0],ptilerng[-1]], [y,y],color = color,linewidth=2,clip_on = False,alpha=0.4)

    ybox = np.array([-1,-1,1,1])*.4+y
    plt.fill([ptilerng[1],ptilerng[3],ptilerng[3],ptilerng[1]],
             ybox, color = color,clip_on = False)
    plt.plot(ptilerng[2]+np.zeros(2),ybox[1:3],'k',alpha=0.3,clip_on = False)
    if islabel: #centertext
        txt = plt.text(np.nanmean(ptilerng),y,f' {rightlabel}',
             fontsize='x-small',alpha = 0.7,
             horizontalalignment = 'center',
             verticalalignment='center',clip_on = False)
    else:
        #return
        txt = plt.text(np.nanmax(ptilerng),y,f' {rightlabel}',
             fontsize='xx-small',alpha = 0.3,verticalalignment='center',clip_on = False)
        output.append(newrow)

    txt.set_path_effects([PathEffects.withStroke(linewidth=2, alpha=0.3, foreground='w')])


fig1 = plt.figure(figsize = [4,6], facecolor='white', dpi=300)
plt.gca().set_frame_on(False)
plt.gca().axes.get_yaxis().set_visible(False)
plt.xlim([-.5, 9.2])
plt.gca().set_axisbelow(True)

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
        elif component == 'All but GIC':
            subset = iceemu[iceemu.ice_component != 'GIC']
        else:
            continue
        g = subset.groupby(['model_key','startyr','endyr'], as_index = False)
        subset = g.agg({'TSLS': np.sum})
        if component in ['GMSL', 'All but GIC']:
            #at this point subset is land_ice - now add steric
            for index, row in subset.iterrows():
                s = steric[(steric.startyr == row.startyr) & (steric.endyr == row.endyr)]
                #s = s[s.model_key == np.random.choice(s.model_key.unique())]
                stericTSLS = s.TSLS.sample(1).values
                subset.at[index,'TSLS'] = subset.at[index,'TSLS'] + stericTSLS


    #MODELS
    for startyr, group in subset.groupby('startyr'):
        if group.shape[0]<2:
            continue
        ps = np.percentile(group.TSLS*1000,ptiles)
        lbl = f'{group.startyr.iloc[0]}-{group.endyr.iloc[0]}'
        myboxplot(yrow,ps,name='models',component=component,rightlabel=lbl)
        yend = yrow
        yrow = yrow + 1


    #OBS
    if component in comparisondata.index:
        subset_obs = comparisondata.loc[component]
        mu = subset_obs.TSLS*1000
        sigma = subset_obs.sigmaTSLS*1000
        ps= [subset_obs.TSLS_P5, subset_obs.TSLS_P17, subset_obs.TSLS_P50, subset_obs.TSLS_P83, subset_obs.TSLS_P95]
        lbl = f"{subset_obs['period start']:.0f}-{subset_obs['period end']:.0f}"
        myboxplot(yrow,np.array(ps)*1000,'observations',component,lbl)
        yend = yrow
        yrow = yrow + 1

    #experts
    ex = experts.loc[experts.Component == component]
    if len(ex)==2:
        dT = np.diff(ex['avgT during 21stC'].values,axis=0)[0]
        Sdot = ex[['SLR 5', 'SLR 17', 'SLR 50', 'SLR 83', 'SLR 95']]*10
        dSdot_dT = np.diff(Sdot.values,axis=0)[0]/dT
        myboxplot(yrow,dSdot_dT,'experts',component,'2000-2100')
        yend = yrow
        yrow = yrow + 1


    plt.text(-.8,(yend+ystart)/2,component,horizontalalignment='right',verticalalignment='center')

        # x = np.linspace(plt.xlim()[0],plt.xlim()[1],1000)
        # y = norm.pdf(x, loc=subset_obs.TSLS*1000, scale=subset_obs.sigmaTSLS*1000)
        # y = y*plt.ylim()[1]/np.max(y)
        # plt.plot(x, y, 'k', label = f"{subset_obs['period start']:.0f}-{subset_obs['period end']:.0f} obs")


rng =[np.nan,6.1,np.nan,9,np.nan]
myboxplot(1.5,rng, '1850-2014', rightlabel='models historical', islabel=True)
myboxplot(2.5,rng, '2016-2050', rightlabel='models early $21^{st}$C', islabel=True)
myboxplot(3.5,rng, '2051-2100', rightlabel='models late $21^{st}$C', islabel=True)
myboxplot(4.5,rng, 'observations', rightlabel='observations', islabel=True)
myboxplot(5.5,rng, 'experts', rightlabel='experts $21^{st}$C', islabel=True)


plt.grid(axis='x',linewidth=0.5,color='#EEEEEE')
plt.xlabel('TSLS (mm/yr/K)')
plt.show()

df = pd.DataFrame(output)


df.to_csv(f'{datafolder}/processed_data/TSLS_estimates/final_tsls_ranges.csv',index=False)
#