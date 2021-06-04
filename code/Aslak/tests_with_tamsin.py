# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 13:20:38 2021

@author: ag
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



file = "../../data/raw_data/Landice-Edwards21/proj_MAIN_TIMESERIES/projections_FAIR_SSP119.csv"
df = pd.read_csv(file)
components = {('GrIS','All'),('AIS','WAIS')}

for component in components:
    ice_source = component[0]
    region = component[1]

    V = df[(df.ice_source == ice_source)]
    V.collapse = V.collapse.fillna(0)  # Replace empty na values with zeros...

    if not region:
        # Empty region means sum all regions.
        V = (
            V.groupby(by=["sample", "year", "collapse"])
            .agg({"SLE": "sum", "GSAT": "mean"}, as_index=False)
            .reset_index()
        )

    Q = V.groupby(by=["sample","collapse"])

    Ts=[]
    for sampleix, sample in Q:
        t = sample.year.values
        T = sample.GSAT.values #- T2015  # Apply base-line correction
        period = np.array([2016,2050])
        ix = period - t[0]
        Tavg = np.mean(T[ix[0] : ix[-1] + 1])
        Ts.append(Tavg)
    print(t)
    print(np.median(np.array(Ts)))
    1/0

    Q=V[(V.year>=2016) & (V.year<=2050)]
    Q = Q.groupby(by=["sample"]).agg({'GSAT': 'mean'}).reset_index()
    print(Q.GSAT.median())



