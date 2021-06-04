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

# distinctcolors = ['#e6194B', '#3cb44b', '#ffe119','#4363d8', '#f58231', '#42d4f4', '#f032e6', '#fabebe', '#469990', '#e6beff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#000075', '#a9a9a9', '#ffffff', '#000000']

scenariocolors = {
    "SSP119": "#e6194B",
    "SSP126": "#3cb44b",
    "SSP245": "#ffe119",
    "SSP370": "#4363d8",
    "SSP585": "#f58231",
    "SSPNDC": "#42d4f4",
}


def extractRateVsT(
    ice_source="Glaciers",
    region="",
    risk_averse=False,
    targetperiods=np.array([[2016, 2050], [2051, 2100]]),
    loadifavailable = True,
):

    filename = "../../data/processed_data/ExtractedFromTamsin/{}_{}_risk{}.csv".format(
        ice_source, region, risk_averse
    )

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
            T = sample.GSAT.values + T2015  # Apply base-line correction

            SLE = (
                savgol_filter(sample.SLE.values/100, 15, 1)
            )  # visually 15 year smoothing looks sensible.
            for periodix in range(targetperiods.shape[0]):
                period = targetperiods[periodix, :]
                ix = period - t[0]
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


def plotScatter(output):
    ice_source = output.iloc[0].ice_source
    region = output.iloc[0].region
    if len(region)<2:
        region = None
    G = output.groupby(["scenario", "startyr", "endyr"])
    for groupix, g in G:
        scenario = groupix[0]
        col = scenariocolors[scenario]
        # plt.scatter(g.Tavg, g.dSdt*100, c=col, s=2, alpha=.5)
        plt.scatter(
            g.Tavg.median(),
            g.dSdt.median() * 100,
            c=col,
            s=50,
            zorder=10,
            edgecolors="k",
            label=scenario,
        )

    # ------------ PLOT comparison data --------------
    if region:
        sheet_name = region
    else:
        sheet_name = ice_source
    print(sheet_name)
    comparison_data = pd.read_excel(
        "../../data/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx",
        sheet_name=sheet_name,
        skiprows=3,
    )
    for ix, row in comparison_data.iterrows():
        Trow = hadcrut5.getTstats(row["Period start"], row["Period end"])
        plt.errorbar(
            Trow["Tanom"],
            row["Rate"],
            xerr=Trow["sigmaT"],
            yerr=row["RateSigma"],
            c="k",
        )
        plt.text(Trow["Tanom"], row["Rate"] - row["RateSigma"], row["Name"])

    plt.title("{} {}".format(ice_source, region))
    plt.xlabel("mean T")
    plt.ylabel("dSdt (m/century)")
    plt.legend()

AIS = extractRateVsT(ice_source="AIS", region="", risk_averse=False)
GrIS = extractRateVsT(ice_source="GrIS", region="", risk_averse=False)
Glaciers = extractRateVsT(ice_source="Glaciers", region="", risk_averse=False)
Pen = extractRateVsT(ice_source="AIS", region="PEN", risk_averse=False)
EAIS = extractRateVsT(ice_source="AIS", region="EAIS", risk_averse=False)
WAIS = extractRateVsT(ice_source="AIS", region="WAIS", risk_averse=False)

# EAIS = extractRateVsT(ice_source="AIS", region="EAIS", risk_averse=True)
# WAIS = extractRateVsT(ice_source="AIS", region="WAIS", risk_averse=True)
# Pen = extractRateVsT(ice_source="AIS", region="Pen", risk_averse=True)
# AIS = extractRateVsT(ice_source="AIS", region="", risk_averse=True)

plotScatter(Pen)


