import numpy as np
import pandas as pd
import tas_tools
from settings import datafolder, targetperiods_future, baseline_period
import glob

scenario = ['ssp585','ssp126','ssp585','ssp585','ssp585']
model = ['CNRM-CM6-1','CNRM-CM6-1','UKESM1-0-LL','CESM2','CNRM-ESM2-1']
run = ['r1i1p1f2','r1i1p1f2','r1i1p1f2','r4i1p1f1','r1i1p1f2']
output = []
for i in range(0,len(model)):
    print(scenario[i],model[i],run[i])
    tas = tas_tools.load_tas(model = model[i],scenario = scenario[i], run = run[i]+'_gr')
    trun = run[i]+'_gr'
    if (tas is None):
        tas = tas_tools.load_tas(model = model[i],scenario = scenario[i], run = run[i]+'_gn')
        trun = run[i]+'_gn'
    tas_his =  tas_tools.load_tas(model = model[i], scenario = "historical", run = trun)
    Tbase = np.mean(tas_his.loc[baseline_period[0]:baseline_period[1]].values)
    for periodix in range(targetperiods_future.shape[0]):
        period = targetperiods_future[periodix,:]
        Tavg = np.nanmean(tas.loc[period[0]:period[-1]].values) - Tbase
        newrow = {
                "model": model[i],
                "run": trun,
                "scenario": scenario[i],
                "startyr":period[0],
                "endyr":period[-1],
                "Tavg":Tavg,}
        output.append(newrow)

output = pd.DataFrame(output)


print(output)
fout = f'{datafolder}/processed_data/CMIP6_tas_for_GrIS.csv'
output.to_csv(fout)
