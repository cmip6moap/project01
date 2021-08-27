


import numpy as np
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import corner
import hadcrut5
import os



steric = pd.read_csv('../../data/processed_data/ExtractedFromSSH/StericTvsRate.csv')


tfolder = '../../data/processed_data/ExtractedFromTamsin/'
ice = {'WAIS': None,
        'EAIS': None,
        'PEN': None,
        'Glaciers': None,
        'GrIS': None}

risk = False

for tfile in ice:
    fname = f'{tfolder}{tfile}_risk{risk}.csv'
    if not os.path.isfile(fname):
        fname = fname.replace('True','False')
    ice[tfile] = pd.read_csv(fname)





#OUTPUT dataframe
#model

output = pd.DataFrame(
    columns=[
        "model",
        "scenario",
        "startyr",
        "endyr",
        "run",
        "Tavg",
        "Tavg_ice",
        "run",
        "ice_sample",
        "risk_averse",
        "Steric",
        "WAIS",
        "EAIS",
        "PEN",
        "Glaciers",
        "GrIS",
    ]
)


scenarios = ['SSP126', 'SSP245', 'SSP585']
targetperiods = np.array([[2016,2050],[2051,2100]])

for scenario in scenarios:
    Ssub1 = steric[steric.scenario == scenario]
    for model in tqdm(Ssub1.model.unique()):
        Ssub2 = Ssub1[Ssub1.model == model]
        for periodix in range(targetperiods.shape[0]):
            period = targetperiods[periodix, :]
            #---
            S = Ssub2[(Ssub2.startyr==period[0]) & (Ssub2.endyr==period[1])]
            for ix in range(10):
                s = S.sample().iloc[0]

                Pen = ice['PEN']
                Pen = Pen[Pen['scenario'] == scenario]
                P = Pen[np.abs(s.Tavg - Pen.Tavg)<0.05]
                if len(P)==0:
                    mix = np.argmin(s.Tavg - Pen.Tavg)
                    p = Pen.iloc[mix]
                else:
                    p = P.sample().iloc[0]
                newrow = {
                    "model": model,
                    "scenario": scenario,
                    "startyr": period[0],
                    "endyr": period[1],
                    "Tavg": s.Tavg,
                    "Tavg_ice": p.Tavg,
                    "run": s.run,
                    "ice_sample": p['sample'],
                    "risk_averse": risk,
                    "Steric": s.dSdt,
                    "WAIS": ice['WAIS'].loc[p.name].dSdt,  #NOTE THIS ASSUMES matching order between files!!!!
                    "EAIS": ice['EAIS'].loc[p.name].dSdt,
                    "PEN": p.dSdt,
                    "Glaciers": ice['Glaciers'].loc[p.name].dSdt,
                    "GrIS": ice['GrIS'].loc[p.name].dSdt
                }
                output.loc[output.shape[0]] = newrow #EXTREMELY SLOW!


output['AIS'] = output['EAIS'] + output['WAIS'] + output['PEN']
output['GMSL'] = output['Steric'] + output['GrIS'] + output['Glaciers'] + output['EAIS'] + output['WAIS'] + output['PEN']





#------------------plot a component------------------



#df  = output[output.startyr == 2051]
df = output
groups = df.groupby('scenario')


components = ['AIS', 'Steric','WAIS','EAIS','PEN','GrIS','Glaciers','GMSL']

#components= ['GMSL']
for component in components:


    for name, group in groups:
        plt.plot(group["Tavg"], group[component]*100, marker="o", linestyle="", label=name)
    plt.legend()


    #-----------------plot comparison data

    sheet_name = component
    comparison_data = pd.read_excel(
        "../../data/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx",
        sheet_name=sheet_name,
        skiprows=3,
    )
    for ix, row in comparison_data.iterrows():
        Trow = hadcrut5.getTstats(row["Period start"], row["Period end"])
        plt.errorbar(
            Trow["Tanom"],
            row["Rate"],
            xerr=Trow["sigmaT"],
            yerr=row["RateSigma"],
            c="r",
        )
        plt.text(Trow["Tanom"], row["Rate"] - row["RateSigma"], row["Name"],c='r')

    plt.title(f'd{component}/dt (m/century)')
    plt.xlabel(f'Tavg')

    plt.show()

1/0



#UGLY HACK

import pickle
from scipy.stats.stats import pearsonr

def loadpickle(fname):
    with open(fname, 'rb') as f:
        return pickle.load(f)


dTnewbaseline = hadcrut5.getTstats(1986, 2015)['Tanom']


std2likely = 0.95417
std290 = 1.6449

distinctcolors = ['#e6194B', '#4363d8', '#f58231', '#42d4f4', '#f032e6', '#fabebe', '#469990', '#e6beff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#000075', '#a9a9a9', '#ffffff', '#000000']

ar5 = loadpickle('../../data/raw_data/AR5 data used in paper/13.SM.1/AR5.pickle')
srocc = loadpickle('../../data/raw_data/SROCC data/SM4.2/SROCC-AR5.pickle')



#colsize=4
#plt.figure(figsize=np.array((1.0,0.7))*colsize,dpi=150)

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
    T = item['temperature'] + dTnewbaseline
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
    T = item['temperature'] + dTnewbaseline
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


plt.xlabel('Time-averaged GMST anom (K)')
plt.ylabel('dSdt (m/century)')



# ------------ PLOT comparison data --------------
sheet_name = 'GMSL'
comparison_data = pd.read_excel(
    "../../data/raw_data/ComparisonEstimates/ComparisonSLRrates.xlsx",
    sheet_name=sheet_name,
    skiprows=3,
)
for ix, row in comparison_data.iterrows():
    Trow = hadcrut5.getTstats(row["Period start"], row["Period end"])
    plt.errorbar(
        Trow["Tanom"],
        row["Rate"],
        xerr=Trow["sigmaT"],
        yerr=row["RateSigma"],
        c="r",
    )
    plt.text(Trow["Tanom"], row["Rate"] - row["RateSigma"], row["Name"],c='r')


