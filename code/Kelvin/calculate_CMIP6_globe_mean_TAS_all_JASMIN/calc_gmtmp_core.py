import sys
import csv
import numpy as np
import pandas as pd
import os
from pathlib import Path
import get_cmip_path_v2
import xarray as xr
import core_component as cc


## Read from shell script
ii = int(sys.argv[1])
mip=sys.argv[2]
expr=sys.argv[3]

##**********************************************************
## TEST code
## INPUT
#mip="CMIP"	##CMIP or ScenarioMIP
#ii = 1
#expr='historical' ## historical or ssp126 or ssp245 or ssp585
##**********************************************************

with open('file_list/file_list_'+expr+'.csv') as file:
	path_list = file.readlines()
	path_list = [line.rstrip() for line in path_list]

tpath = path_list[ii]
dum = tpath.split('/')
fname = 'gm_tas_'+mip+'_'+expr+'_'+dum[7]+'_'+dum[9]+'_'+dum[12]+'.csv'
file_list = []
for cp, cd, cf in os.walk(tpath):
	for f in cf:
		file_list.append(os.path.join(tpath,f))

flag = 0
for ff in file_list:
#	flag = 0
	ds = xr.open_dataset(ff)	
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
output_fin.to_csv('./'+expr+'/'+fname,sep=",",index=False)
#
