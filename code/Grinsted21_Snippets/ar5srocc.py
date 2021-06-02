
#
# extract GMSL rate values from AR5 and SROCC
#
#


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from scipy.stats.stats import pearsonr


def loadpickle(fname):
    with open(fname, 'rb') as f:
        return pickle.load(f)




std2likely = 0.95417
std290 = 1.6449

distinctcolors = ['#e6194B', '#4363d8', '#f58231', '#42d4f4', '#f032e6', '#fabebe', '#469990', '#e6beff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#000075', '#a9a9a9', '#ffffff', '#000000']

ar5 = loadpickle('../../data/raw_data/AR5 data used in paper/13.SM.1/AR5.pickle')
srocc = loadpickle('../../data/raw_data/SROCC data/SM4.2/SROCC-AR5.pickle')



colsize=4
plt.figure(figsize=np.array((1.0,0.7))*colsize,dpi=150)

naming = {'05': 'low', '50': 'mid', '95': 'upper'}

TSLS = pd.DataFrame(columns=('name', 'mid', 'low', 'upper'))
TSLS.set_index('name',inplace=True)
BalanceT = pd.DataFrame(columns=('name', 'mid', 'low', 'upper'))
BalanceT.set_index('name',inplace=True)
Intercept = pd.DataFrame(columns=('name', 'mid', 'low', 'upper'))
Intercept.set_index('name',inplace=True)
colnames={0: 'low', 1:'mid', 2:'upper'}

#------------------------------------------AR5
color=distinctcolors[0]
xy = []
xx2 = dict()
for scenario,item in ar5.items():
    SL = item['sum'].loc[2100]-item['sum'].loc[2000]
    T = item['temperature']
    T = T.loc[2000:2100].mean()
    plt.plot([T.low,T.mid, T.upper],[SL.low,SL.mid,SL.upper],color=color,alpha=0.5,linewidth=2)
    plt.plot(T.mid,SL.mid,'x',markersize=10,markeredgewidth=2,color=color)
    xy.append([[T.low,T.mid, T.upper],[SL.low,SL.mid,SL.upper]])


plt.annotate('$\mathrm{AR5}$',(2.5,0.77),color=color,
             horizontalalignment='center', verticalalignment='center',
             rotation=22)


xy=np.array(xy)
for col in range(3):
    p=np.polyfit(xy[:,0,col],xy[:,1,col],1)
    T0=-p[1]/p[0]
    print('AR5 slope \t {:.2f}   \tT0={:.2f}'.format(p[0],T0))
    TSLS.at['AR5',colnames[col]]=p[0]
    BalanceT.at['AR5',colnames[col]]=T0
    Intercept.at['AR5',colnames[col]]=p[1]

print('pearsonR AR5', pearsonr(xy[:,0,:].ravel(),xy[:,1,:].ravel()))
print('pearsonR AR5 mid', pearsonr(xy[:,0,1].ravel(),xy[:,1,1].ravel()))

#------------------------------------------SROCC
xy = []
color=distinctcolors[1]
for scenario,item in srocc.items():
    SL = item['sum'].loc[2100]-item['sum'].loc[2000]
    T = item['temperature']
    T = T.loc[2000:2101].mean()
    xy.append([[T.low,T.mid, T.upper],[SL.low,SL.mid,SL.upper]])
    plt.plot([T.low,T.mid, T.upper],[SL.low,SL.mid,SL.upper],color=color,alpha=0.5,linewidth=2)
    plt.plot(T.mid,SL.mid,'x',markersize=10,markeredgewidth=2,color=color)
plt.annotate('$\mathrm{SROCC}$',(2.5,1.1),color=color,
         horizontalalignment='center', verticalalignment='center',
         rotation=24)


xy=np.array(xy)
for col in range(3):
    p=np.polyfit(xy[:,0,col],xy[:,1,col],1)
    T0=-p[1]/p[0]
    print('SROCC slope \t {:.2f}   \tT0={:.2f}'.format(p[0],T0))
    TSLS.at['SROCC',colnames[col]]=p[0]
    BalanceT.at['SROCC',colnames[col]]=T0
    Intercept.at['SROCC',colnames[col]]=p[1]
