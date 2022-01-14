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



def plot_comparison(sheet_name = 'GMSL', show_experts=False, color='k', show_line = False):

    comparison_data = pd.read_excel(
        f"{datafolder}/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx",
        sheet_name=sheet_name, comment="#"
    )
    lbl='Data'
    for ix, row in comparison_data.iterrows():
        Trow = hadcrut5.getTstats(row["Period start"], row["Period end"])
        plt.errorbar(
            Trow["Tanom"],
            row["Rate"],
            xerr=Trow["sigmaT"],
            yerr=row["RateSigma"],
            c=color,
            marker='o',
            markersize=5,
            markerfacecolor='#777777',
            label=lbl
        )
        plt.text(Trow["Tanom"], row["Rate"] + row["RateSigma"], f' {row["Name"]}',
                 alpha=.6,rotation=90,
                 horizontalalignment='center',
                 verticalalignment='bottom',
                 color=color,
                 fontsize=8)
        lbl = None

    if show_experts:
        experts = pd.read_excel( f"{datafolder}/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx",
            sheet_name='Expert', comment="#"
            )
        experts=experts[experts.Component == sheet_name]
        if len(experts)>0:
            Tbase =hadcrut5.getTstats(1850,1900)
            T = experts['avgT during 21stC'].to_numpy() + Tbase['Tanom']
            S = experts['SLR 50'].to_numpy()*10
            Serr =experts[['SLR 17', 'SLR 83']].to_numpy()*10
            plt.errorbar(T, S,fmt='ro',yerr = np.abs(Serr-np.tile(S,(2,1)).T), xerr = Tbase['tot_sigma'],label='Experts')



if __name__ == "__main__":
    # this is some test code:
    plot_comparison('GMSL')
    plot_comparison('G&C GMSL', color='r')
    plt.legend()