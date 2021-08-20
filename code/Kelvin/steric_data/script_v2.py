import csv
import numpy as np
import matplotlib.pyplot as plt
import array
import pandas as pd
from scipy import stats
##from scipy.ndimage import median_filter  # used for outlier removal
#import steric_tools as st
#import tas_tool.py as tt

import core_extract as ce

##=============================================================================
## INPUT
## Baseline years
ybl_st = 1995
ybl_ed = 2014

expt=['historical','ssp126','ssp245','ssp585']

## Target range
flag = 0
for j in expt:
    print('************************')
    print('Current :',j)
    if j == 'historical':
        yta_st = [1850,1900,1992]
        yta_ed = [1900,1950,2014]
    else:
        yta_st = [2016,2051]
        yta_ed = [2050,2100]
    nrange = len(yta_st)
    for i in range(0,nrange):
        tmp = ce.extract_steric_v1(j,yta_st[i],yta_ed[i],ybl_st,ybl_ed)
        if flag == 0:
            final = tmp
            flag = 1
        else:
            final = final.append(tmp,ignore_index=True)

print(final)
final.to_csv('steric_full_standard_format.csv',mode='a',sep=",",index=False)
