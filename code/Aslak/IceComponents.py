# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import re
import hadcrut5
import sgolay
from tqdm import tqdm
from scipy.signal import savgol_filter
from settings import baseline_period, targetperiods




def extractRateVsT(
    ice_source = "Glaciers",
    region = "",
    risk_averse = False,
    targetperiods = targetperiods,
    loadifavailable = False,
):

    shortname = ice_source
    if region:
        shortname = region

    filename = f"../../data/processed_data/ExtractedFromTamsin/{shortname}_risk{risk_averse}.csv"

    if loadifavailable & (len(glob.glob(filename))>0):
        output = pd.read_csv(filename)
        return output

    if risk_averse:
        folder = "../../data/raw_data/Landice-Edwards21/proj_S11_RISK_TIMESERIES"
    else:
        folder = "../../data/raw_data/Landice-Edwards21/proj_MAIN_TIMESERIES"

    files = glob.glob(folder + "/projections_*.csv")

    # this gives the 2015 temperature relative to the baseline temp as defined in hadcrut5.
    T2015 = hadcrut5.getTstats(2010, 2019)["Tanom"]

    output = pd.DataFrame(
        columns=[
            "ice_source",
            "region",
            "sample",
            "scenario",
            "riskaverse",
            "startyr",
            "endyr",
            "Tavg",
            "dSdt",
        ]
    )
    for file in tqdm(files):
        scenario = re.findall("_FAIR_([^\.]*)", file)[0]

        V = pd.read_csv(file)
        V = V[V.ice_source == ice_source]
        V.collapse = V.collapse.fillna(0)  # Replace empty na values with zeros...
        # V = V[(V.year>=period[0]) & (V.year<=period[1])]

        if not region:
            # Empty region means sum all regions.
            V = (
                V.groupby(by=["sample", "year"])
                .agg({"SLE": "sum", "GSAT": "mean"}, as_index=False)
                .reset_index()
            )
        else:
            V = V[V["region"] == region]

        Q = V.groupby(by=["sample"])

        for sampleix, sample in tqdm(Q):
            t = sample.year.values
            T = sample.GSAT.values + T2015  # Apply base-line correction (Tamsin says her numbers are relative to 2015. )

            SLE = (
                savgol_filter(sample.SLE.values/100, 15, 1)
            )  # visually 15 year smoothing looks sensible.
            for periodix in range(targetperiods.shape[0]):
                period = targetperiods[periodix, :]
                ix = period - t[0]
                if ix[0]<0:
                    #skip historical periods not in dataset.
                    continue
                dSdt = (SLE[ix[-1]] - SLE[ix[0]]) / (period[-1] - period[0])
                Tavg = np.mean(T[ix[0] : ix[-1] + 1])
                newrow = {
                    "ice_source": ice_source,
                    "region": region,
                    "sample": sampleix,
                    "scenario": scenario,
                    "risk_averse": risk_averse,
                    "startyr": period[0],
                    "endyr": period[-1],
                    "Tavg": Tavg,
                    "dSdt": dSdt,
                }
                output.loc[output.shape[0]] = newrow #EXTREMELY SLOW!

        # Q = Q.agg({'GSAT': 'mean', 'SLE': lambda x: (x.iloc[-5:].mean())*100/(2098-2015)}, as_index=False).reset_index()
        # h=plt.scatter(Q.GSAT+T2015, Q.SLE/100, c=distinctcolors[fileix], s=2, alpha=.5)
        # plt.scatter(Q.GSAT.median()+T2015, Q.SLE.median()/100, c=distinctcolors[fileix], s=50, zorder=10, edgecolors='k', label=scenario)
        output.to_csv(filename)

    return output




AIS = extractRateVsT(ice_source="AIS", region="", risk_averse=False)
GrIS = extractRateVsT(ice_source="GrIS", region="", risk_averse=False)
Glaciers = extractRateVsT(ice_source="Glaciers", region="", risk_averse=False)
Pen = extractRateVsT(ice_source="AIS", region="PEN", risk_averse=False)
EAIS = extractRateVsT(ice_source="AIS", region="EAIS", risk_averse=False)
WAIS = extractRateVsT(ice_source="AIS", region="WAIS", risk_averse=False)

EAIS = extractRateVsT(ice_source="AIS", region="EAIS", risk_averse=True)
WAIS = extractRateVsT(ice_source="AIS", region="WAIS", risk_averse=True)
Pen = extractRateVsT(ice_source="AIS", region="PEN", risk_averse=True)
AIS = extractRateVsT(ice_source="AIS", region="", risk_averse=True)




