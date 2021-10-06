import os

import os
def search_cmip_path(mip,expr):
## CMIP6 on JASMIN
## Structure (number represents the level, 1 as the outer layer)
##	(1) root_path = '/badc/cmip6/data/CMIP6/'	<< This is fixed
##	(2) activity_id = 'CMIP' or 'ScenarioMIP'	<< We are only interested in these 2 anyway
##	(3) institution_id = e.g. 'MOHC'		<< We do search on it
##	(4) source_id = e.g. 'UKESM1-0-LL'		<< Model name, we do search on it
##	(5) expr_id = 'historical' , 'ssp126', 'ssp245', 'ssp585'	<< We specified this
##	(6) variant = e.g. r1i1p1f1			<< We do search on it
##	(7) table_id = 'Amon'				<< FIXED
##	(8) variable = "tas"				<< FIXED
##	(9) grid_label = e.g. 'gr'			<< We do search on it because they are all different
##	(10) fin = 'latest'				<< FIXED
##	(11) SOURCE FILES!!!

## INPUT
#	mip = 'CMIP'
#	expr = 'historical'

## Constant
	cmip_path = '/badc/cmip6/data/CMIP6/'
## Find layer 3, GET the name of all centres
	dum1 = []
	for cpath, dir_layer, files in os.walk(cmip_path+mip):
		for dl in dir_layer:
			dum1.append(dl)
		break
## layer 4
	dum2 = []
	for cc in dum1:
		for cpath, dir_layer, files in os.walk(cmip_path+mip+"/"+cc):
			for dl in dir_layer:
				dum2.append(cc+'/'+dl+'/'+expr)
			break

## layer 6
	dum1 = []
	for cc in dum2:
		for cpath, dir_layer,files in os.walk(cmip_path+mip+'/'+cc):
			for dl in dir_layer:
				dum1.append(cc+'/'+dl+'/Amon/tas')
			break
## layer 8
	dum2 = []
	for cc in dum1:
		for cpath, dir_layer, files in os.walk(cmip_path+mip+'/'+cc):
			for dl in dir_layer:
				dum2.append(cc+'/'+dl+'/latest')
			break
	#print(dum2)
	return(dum2)
## File paths
#	fpath = []
#	for cc in dum2:
#		for cpath, dir_layer, files in os.walk(cmip_path+mip+'/'+cc):
#			for file in files:
#				fpath.append(os.path.join(cpath,file))

