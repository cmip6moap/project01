# Modified Aslak's original script


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import re

def get_data(scen,source,region,minyr,maxyr):
        sl_url = 'https://raw.githubusercontent.com/cmip6moap/project01/main/data/raw_data/Landice-Edwards21/proj_MAIN_TIMESERIES/projections_FAIR_SSP'+scen+'.csv'
        V = pd.read_csv(sl_url);
        V.collapse = V.collapse.fillna(0)
        V = V[(V.ice_source == source) & (V.year <= maxyr) & (V.year>= minyr)]
        if region == "None":
        #None is intended as a wildcard for all regions. Calculate the sum of all
                V = V.groupby(by=['sample','year']).agg({'SLE': 'sum', 'GSAT': 'mean'}, as_index=False).reset_index()
        else:
                V = V[V.region==region]
        Q = V.groupby(by=['sample'])
        Q = Q.agg({'GSAT': 'mean', 'SLE': lambda x: (x.iloc[-5:].mean())*100/(maxyr-minyr+1)}, as_index=False).reset_index()
        return(Q)

distinctcolors = ['#e6194B', '#3cb44b', '#ffe119','#4363d8', '#f58231', '#42d4f4', '#f032e6', '#fabebe', '#469990', '#e6beff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#000075', '#a9a9a9', '#ffffff', '#000000']

msource=['GrIS','AIS','Glaciers']       ## Target source
ssp=["119","126","245","370","585","NDC"]       #ar6=(119 126 245 370 585)

for tsource in msource:
        if tsource == 'AIS':
                iregion=['WAIS','EAIS']
        if tsource == 'GrIS':
                iregion=['ALL']
        if tsource == 'Glaciers':
                iregion=['None']
        for tregion in iregion:
                fileix = 0
                for ii in ssp:
                        Q = get_data(ii,tsource,tregion,2016,2050)
                        print("-----------")
                        print("SSP"+ii)
                        h = plt.scatter(Q.GSAT.median(), Q.SLE.median()/100, c=distinctcolors[fileix], s=50, zorder=10, edgecolors='k', label='SSP'+ii+'(1st)',marker="v")
#                       fileix = fileix + 1

                        Q = get_data(ii,tsource,tregion,2051,2100)
                        print("-----------")
                        print("SSP"+ii)
                        h = plt.scatter(Q.GSAT.median(), Q.SLE.median()/100, c=distinctcolors[fileix], s=50, zorder=10, edgecolors='k', label='SSP'+ii+'(2nd)',marker="^")
                        fileix = fileix + 1

                plt.xlabel('mean T anom')
                plt.ylabel('rate SLE (cm/a)')
                plt.title(tsource+" ("+tregion+")")
                plt.legend()
        #       plt.axis((0,4,0,0.3))
                plt.savefig(tsource+"_"+tregion+"_split_median_only.jpeg")
                plt.close()
        #exit()
                                                                                                              58,1-8        Bot
