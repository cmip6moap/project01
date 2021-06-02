# -*- coding: utf-8 -*-



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import re




files = glob.glob('proj_MAIN_TIMESERIES/projections_*85.csv')
#files = glob.glob('proj_MAIN_TIMESERIES/projections_*.csv')

for file in files:
    scenario = re.findall('_FAIR_([^\.]*)',file)[0]

    V = pd.read_csv(file);
    V.collapse = V.collapse.fillna(0)


    Q= V[(V.ice_source=='GrIS') & (V['sample'] ==301)]
    plt.plot(Q.year,Q.SLE)
    #plt.scatter(Q.GSAT, Q.SLE, c=Q.year)
    plt.title('{} {} sample#{}'.format(scenario, Q.ice_source.iloc[0], Q['sample'].iloc[0]))
    #plt.colorbar()
    plt.xlabel('year')
    plt.ylabel('SLE (cm)')
    1/0


    Q = V.groupby(by=['ice_source','region','sample','collapse'])

    #Q = Q.agg({'GSAT': 'mean', 'SLE': lambda x: x.iloc[-1]}, as_index=False).reset_index()
    Q = Q.agg({'GSAT': 'mean', 'SLE': lambda x: (x.iloc[-1]-x.iloc[0])*100/(2100-2016)}, as_index=False).reset_index()

    q = Q[Q.ice_source=='GrIS']

    scenario = re.findall('_FAIR_([^\.]*)',file)[0]

    plt.scatter(q.GSAT+0.10,q.SLE/100,label=scenario)


plt.xlabel('mean T')
plt.ylabel('SLE_2100')
plt.legend()