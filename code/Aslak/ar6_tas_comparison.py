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

T21 = []
i=0
for f in glob.glob(f'{datafolder}/raw_data/CMIP6_TAS/*_ssp585_i1p1f1_00.dat'):
    tas = pd.read_csv(f,comment='#',index_col=0,delim_whitespace=True,header=None)
    tas = tas.mean(axis=1)
    tas = tas- tas[tas.index<=1900].mean()
    if i==0:
        h = plt.plot(tas,color='b',alpha=0.5,label='CMIP6')
    else:
        h = plt.plot(tas,color='b',alpha=0.5)
    i=i+1

f = f"{datafolder}/raw_data/AR6 Fig spm08ad/tas_global_Historical.csv"
tas_hist =pd.read_csv(f,index_col=0)
scenario = 'SSP5-8.5'
f = f"{datafolder}/raw_data/AR6 Fig spm08ad/tas_global_{scenario.replace('-','_').replace('.','_')}.csv"
tas_proj =pd.read_csv(f,index_col=0)
plt.plot(tas_hist.Mean,color='k',label='AR6 fig. SPM08')
plt.plot(tas_proj,color='k')
plt.xlabel('time')
plt.ylabel('GMST')
plt.legend()
tas_proj.iloc[-1]
