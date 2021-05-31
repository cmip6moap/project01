# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 14:02:59 2019

@author: ag
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 12:36:44 2019

@author: ag
"""

import numpy as np
import re
from scipy import interpolate
import pandas as pd
import pickle

def loadfile(txt):
    df = pd.read_csv(txt,delim_whitespace=True)
    df.columns = df.columns.str.strip()

    #remove 20year means in bottom of file.
    ix = df.index[df.year.apply(lambda x: not x.isnumeric())]
    if len(ix)>0:
        ix=ix[0]
        df=df.iloc[0:ix]
    df.year=pd.to_numeric(df.year)
    df['05']=pd.to_numeric(df['05'])

    df = df.append({'year': 1995.5, '05': 0.0, '50':0.0, '95':0.0},ignore_index=True)
    df.set_index('year',inplace=True)
    
    add = pd.DataFrame({'year': np.arange(1996,2007), '50': np.nan})
    add.set_index('year',inplace=True)
    df= pd.concat((df,add),sort=False)
    df = df.loc[~df.index.duplicated(keep='first')]
    df.sort_index(inplace=True)
    df.interpolate(inplace=True)
    
#    V = np.append(V, [[1995.5,0]], axis=0) # baseline: 1986–2005
    
#    f = interpolate.interp1d(V[:,0], V, axis=0, fill_value='extrapolate',bounds_error=0)
#    V= f(np.arange(2000,2101)) #ensure that it has exactly this period! Some files goes to 2099
    return df
    
    
output={}

d=['ant_26','ant_45','ant_85','gmsl_26','gmsl_45','gmsl_85']
for ii,filename in enumerate(d):
    (component,scenario)=re.findall(r'(.*)_(\d+)',filename)[0]
    
    df = loadfile(filename)
   
    if scenario not in output:
        output[scenario] = {}
    if component not in output[scenario]:
        output[scenario][component] = {}
    output[scenario][component]=df


with open('SROCC.pickle', 'wb') as file:
    pickle.dump(output, file)



#-------------------JOIN WITH AR5--------------------------
ar5 = loadpickle('../../AR5datafiles/13.SM.1/AR5.pickle')

naming = {'26': 'rcp26', '45': 'rcp45', '85': 'rcp85'}
for k,v in naming.items():
    output[v] = output.pop(k)

   
naming = {'05': 'low', '50': 'mid', '95': 'upper'}
for scen,sitem in output.items():
    for contrib,item in sitem.items():
        for k,v in naming.items():
            item[v] = item.pop(k)

naming = {'ant': 'antnet', 'gmsl': 'sum'}
for scenario,item in output.items():
    for k,v in naming.items():
        item[v] = item.pop(k)
    item['temperature'] = ar5[scenario]['temperature']
    
    
with open('SROCC-AR5.pickle', 'wb') as file:
    pickle.dump(output, file)