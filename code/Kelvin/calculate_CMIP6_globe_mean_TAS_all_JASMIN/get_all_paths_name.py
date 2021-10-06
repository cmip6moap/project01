import sys
import csv
import numpy as np
import pandas as pd
import os
from pathlib import Path
import get_cmip_path_v2
import xarray as xr
import core_component as cc


## Note
##	GET all available paths to the target files

## INPUT
mip="ScenarioMIP"	##CMIP or ScenarioMIP
expr='ssp585' ## historical or ssp126 or ssp245 or ssp585

cmip_path = '/badc/cmip6/data/CMIP6/'+mip+'/'
dpath_list = get_cmip_path_v2.search_cmip_path(mip,expr)

file_list = []
for path in dpath_list:
	print(path)
	dum = path.split('/')
	fname = 'gm_tas_'+mip+'_'+expr+'_'+dum[1]+'_'+dum[3]+'_'+dum[6]+'.csv'
	file_list.append(cmip_path+path)
with open('./file_list/file_list_'+expr+'.csv','a') as f:
	for item in file_list:
		f.write(item+'\n')

