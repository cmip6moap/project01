# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:36:44 2019

@author: ag
"""

import numpy as np
import pandas as pd
import glob
import re
from scipy import interpolate
import pickle

def loadfile(txt):
    V = np.loadtxt(txt)
    V = np.append(V, [[1995.5,0]], axis=0) # baseline: 1986–2005
    f = interpolate.interp1d(V[:,0], V, axis=0, fill_value='extrapolate',bounds_error=0)
    V= f(np.arange(2000,2101)) #ensure that it has exactly this period! Some files goes to 2099
    return V
    
    
output={}

d=glob.glob('*lower.txt')
for ii,f_low in enumerate(d):
    f_upper=f_low.replace('lower','upper')
    f_mid=f_low.replace('lower','mid')
    (scenario,component)=re.findall(r'(.*)_(.*)lower',f_low)[0]
    
    low= loadfile(f_low)
    mid= loadfile(f_mid)
    upper= loadfile(f_upper)
    t=low[:,0]
    #V=np.vstack((low[:,1], mid[:,1], upper[:,1])).T
    
    df=pd.DataFrame({'year':t, 'low': low[:,1], 'mid': mid[:,1], 'upper': upper[:,1]})
    df.set_index('year',inplace=True)
    
    if scenario not in output:
        output[scenario] = {}
    if component not in output[scenario]:
        output[scenario][component] = {}
    output[scenario][component]=df


with open('AR5.pickle', 'wb') as file:
    pickle.dump(output, file)
