# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 13:33:35 2021

@author: ag
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import hadcrut5
from settings import datafolder



def plot_comparison(sheet_name = 'GMSL'):

    comparison_data = pd.read_excel(
        f"{datafolder}/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx",
        sheet_name=sheet_name, comment="#"
    )
    for ix, row in comparison_data.iterrows():
        Trow = hadcrut5.getTstats(row["Period start"], row["Period end"])
        plt.errorbar(
            Trow["Tanom"],
            row["Rate"],
            xerr=Trow["sigmaT"],
            yerr=row["RateSigma"],
            c="k",
            marker='o',
            markersize=5,
            markerfacecolor='#777777'
        )
        plt.text(Trow["Tanom"], row["Rate"] + row["RateSigma"], f' {row["Name"]}',alpha=.6,rotation=90,horizontalalignment='center',verticalalignment='bottom',fontsize=8)



if __name__ == "__main__":
    # this is some test code:
    plot_comparison('GIC')