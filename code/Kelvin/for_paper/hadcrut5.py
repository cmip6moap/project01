#
# We need to extract GMST for different periods with respect to a baseline period.
# We also need uncertainties of these estimates.
#
# HadCRUT is nice for this because they provide an ensemble of different temperatures
#
#
# Aslak Grinsted 2021

import pandas as pd
import numpy as np
from settings_v2 import baseline_period

H = pd.read_csv(
    "/rds/projects/l/leckebgc-pre-cax/ngks/cop26_bristol/project01/data/raw_data/HadCRUT5/HadCRUT.5.0.1.0.analysis.ensemble_series.global.annual.csv",
    index_col="Time",
)
T = H.filter(regex="Realization")
C = H["Coverage uncertainty (1 sigma)"]

baseline_start = baseline_period[0]  # https://www.mountainresearchinitiative.org/news-page-all/129-mri-news/2357-call-for-participation-contributions-ipcc-ar6-climate-change-2021-impacts-adaptation-and-vulnerability
baseline_end = baseline_period[1]


def getTstats(startyr, endyr):
    """
    usage: getTstats(startyr, endyr)

    returns a dict with items:
        Tanom: average temperature over period
        sigmaT: hadcrut ensemble std dev of that estimate
        cov_sigma: coverage uncertainty - NEEDS MORE THINKING
        tot_sigma: total uncertainty in Tanom - NEEDS MORE THINKING
    """
    # get the temperature

    Q = T.loc[startyr:endyr].mean() - T.loc[baseline_start:baseline_end].mean()

    deltaT = Q.mean()
    sigmaT = Q.std()

    H["Coverage uncertainty (1 sigma)"]

    # todo: How do we estimate the coverage uncertainty of a period-average?
    cbase = C.loc[baseline_start:baseline_end].mean()
    cperiod = C.loc[startyr:endyr].mean()

    # if two periods are well separated in time then it is reasonable to assume
    # zero covariance between periods.
    cov_sigma = np.sqrt(cbase ** 2 + cperiod ** 2)

    #
    tot_sigma = np.sqrt(sigmaT ** 2 + cbase ** 2 + cperiod ** 2)

    return {
        "Tanom": deltaT,
        "sigmaT": sigmaT,
        "cov_sigma": cov_sigma,
        "tot_sigma": tot_sigma,
    }


if __name__ == "__main__":
    # this is some test code:
    df = pd.read_excel(
        "/rds/projects/l/leckebgc-pre-cax/ngks/cop26_bristol/project01/data/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx",
        sheet_name="GMSL",
        skiprows=3,
    )
    for ix, row in df.iterrows():
        print(row["Name"], getTstats(row["Period start"], row["Period end"]))
