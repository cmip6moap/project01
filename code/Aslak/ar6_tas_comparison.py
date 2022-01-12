# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 12:14:51 2021

@author: ag
"""


import numpy as np
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import corner
import hadcrut5
import re
import os
from settings import scenariocolors, baseline_period, datafolder
from misc_tools import confidence_ellipse
from plot_comparison_data import plot_comparison
import glob


scenarios = {'SSP1-1.9': [],
             'SSP1-2.6': [],
             'SSP2-4.5': [],
             'SSP3-7.0': ,
             'SSP5-8.5':}
for scenario in scenarios:
    tasfile = f"{datafolder}/raw_data/AR6 Fig spm08ad/tas_global_{scenario.replace('-','_').replace('.','_')}.csv"
    tas =pd.read_csv(tasfile)


if True:
    Sar6 = pd.read_csv(f"{datafolder}/raw_data/AR6 Fig spm08ad/global_sea_level_projected.csv",index_col='Year')
    scenarios = ['SSP1-1.9', 'SSP1-2.6', 'SSP2-4.5', 'SSP3-7.0', 'SSP5-8.5']
    tasfile = f"{datafolder}/raw_data/AR6 Fig spm08ad/tas_global_Historical.csv"
    tas =pd.read_csv(tasfile)
    tasbase = tas[(tas.Year>=baseline_period[0]) & (tas.Year<=baseline_period[1])].mean()
    for scenario in scenarios:
        tasfile = f"{datafolder}/raw_data/AR6 Fig spm08ad/tas_global_{scenario.replace('-','_').replace('.','_')}.csv"
        tas =pd.read_csv(tasfile)
        s = Sar6[f'{scenario} Central']
        dSdt = (s[2100]-s[2050])/50
        t = tas[(tas.Year>=2050) & (tas.Year<=2100)].mean() - tasbase
        plt.plot(t['Mean'],dSdt*1000,'bo')
        # dSdt = (s[2050]-s[2020])/30
        # t = tas[(tas.Year>=2020) & (tas.Year<=2050)].mean() - tasbase
        # plt.plot(t['Mean'],dSdt*1000,'mo')
        # dSdt = (s[2100]-s[2020])/70
        # t = tas[(tas.Year>=2020) & (tas.Year<=2100)].mean() - tasbase
        # plt.plot(t['Mean'],dSdt*1000,'ro')
