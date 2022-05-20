# -*- coding: utf-8 -*-
"""
Created on Fri May 20 09:58:09 2022

@author: ag
"""


#extract the GMSL difference from 1850-1900. Kemp et al 2018

import pandas as pd
import numpy as np

df = pd.read_csv('GSL_100y_TG+GSL+PX+flat_TG+GSL+PX+flat_GMML-2tsx3ss_lb.tsv', sep='\t', index_col='Year', skipfooter=441-215,engine='python')
dfcov = pd.read_csv('GSL_TG+GSL+PX+flat_TG+GSL+PX+flat_GMML-2tsx3ss_lb_cov.tsv', sep='\t', index_col="mm^2")

C=np.empty((2,2))
C[0,0]=dfcov.loc[1850]['1850']
C[0,1]=dfcov.loc[1850]['1900']
C[1,0]=dfcov.loc[1900]['1850']
C[1,1]=dfcov.loc[1900]['1900']


dS = df.loc[1900].mm-df.loc[1850].mm

#uncertainty of the difference: (5.21 here:https://www.probabilitycourse.com/chapter5/5_3_1_covariance_correlation.php)
var_dS = C[0,0] + C[1,1] - 2*C[0,1]

sigma_dS = np.sqrt(var_dS)
dt=50


print(f'{dS/dt:.2f}±{sigma_dS/dt:.2f} mm/yr')