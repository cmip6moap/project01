import sys
import csv
import numpy as np
import pandas as pd
import os
from pathlib import Path
import get_cmip_path
import xarray as xr
import core_component as cc


## Read from shell script

k=int(sys.argv[1])
mip=sys.argv[2]
expr=sys.argv[3]

##**********************************************************
## TEST code
## INPUT
#k = 3	
#mip="ScenarioMIP"	##CMIP or ScenarioMIP
#expr='ssp585' ## historical or ssp126 or ssp245 or ssp585
##**********************************************************


modelnames = pd.read_csv('/home/users/ngks/cop26_bristol/script/for_rory/namelist/cmip6_'+mip+'_'+expr+'_strh_zostoga_gm_list.txt', sep = '\s+', names=['no','model','run','val1','val2'], index_col='no')

nrun = len(modelnames.model)
tmodel = list(modelnames.model)
trun_raw = list(modelnames.run)
trun = [i.split('_')[0] for i in trun_raw]
grid_type = [i.split('_')[1] for i in trun_raw]

## Input section
var_resol = 'Amon'		## Variable type and resolution
var_name = 'tas'		## Variable name!


ofname = './'+expr+'/gm_tas_'+mip+'_'+expr+'_'+tmodel[k]+'_'+trun[k]+'_'+grid_type[k]+'.csv'

if os.path.exists(ofname):
	exit()

print('Current :'+ofname)
## Get data path
dpath = get_cmip_path.get_cmip_path(mip,expr,tmodel[k],trun[k],var_resol,var_name,grid_type[k])
print(dpath)
nfile = len(dpath)
print(nfile)
flag = 0
for i in range(0,nfile):
	ds = xr.open_dataset(dpath[i])	
	n_time = len(ds['time'][:])	## Number of time entry
	tavg_tmp = np.zeros(n_time)		## Output array
	atime_tmp = ds['time'][:]	## Everything is in datetime64 array format
	atime_decode = atime_tmp.values.astype('datetime64[s]').tolist()	## Convert to list of datetime elements
	time_tmp = [i.strftime('%Y%m') for i in atime_decode] ## For each datetime elements, we convert it into yyyymm
	grid_cell_area = cc.area_grid(ds['lat'].values, ds['lon'].values)
	total_area_of_earth = grid_cell_area.sum(['lat','lon'])
	for j in range(0,n_time):
		weighted_mean = ((ds['tas'][j,:,:] * grid_cell_area) / total_area_of_earth).sum(['lat','lon'])
		tavg_tmp[j] = weighted_mean

	if flag == 0:
		tavg_out = tavg_tmp
		time_out = time_tmp
		flag = 1
	else:
		time_out = np.append(time_out,time_tmp)
		tavg_out = np.append(tavg_out,tavg_tmp)	


output_pd = {'time':time_out,
	'gm_tas':tavg_out}

output_fin = pd.DataFrame(output_pd)
output_fin.to_csv('./'+expr+'/gm_tas_'+mip+'_'+expr+'_'+tmodel[k]+'_'+trun[k]+'_'+grid_type[k]+'.csv',sep=",",index=False)

