import os

## mip = CMIP or ScenarioMIP
## expr = Experiment
## target_model = model
## target_expr = Experiment
## target_run = Ensemble
## var_resol = variable type and resolution
## var_name = variable name!
## target_gtype = Grid type


def get_cmip_path(mip,expr,target_model,target_run,
		var_resol,var_name,target_gtype):
	cmip_path = '/badc/cmip6/data/CMIP6/'+mip
	print("------------------------------------")
	print("Search path")
## Find the path to model directory
	path2 = []
	for subdir, dirs, files in os.walk(cmip_path):
		for file in dirs:
			if file == target_model:
				path2.append(os.path.join(subdir,file))
				print('Level 1:')
				print(path2)
				break
## Find the path to expr directory
	path3 = []
	for i in range(0,len(path2)):
		for subdir, dirs, files in os.walk(path2[i]):
			for file in dirs:
				if file == expr:
					path3.append(os.path.join(subdir,file))
					print('Level 2:')
					print(path3)
					break
## Find the path to model run directory
	path4 = []
	for i in range(0,len(path3)):
		for subdir,dirs,files in os.walk(path3[i]):
			for file in dirs:
				if file == target_run:
					path4.append(os.path.join(subdir,file))
					print('Level 3:')
					print(path4)
					break
## Find the path to the variable type
	path5 = []
	for i in range(0,len(path4)):
		for subdir,dirs,files in os.walk(path4[i]):
			for file in dirs:
				if file == var_resol:
					path5.append(os.path.join(subdir,file))
					print('Level 4:')
					print(path5)
					break
## Find the path to the variable
	path6 = []
	for i in range(0,len(path5)):
		for subdir,dirs,files in os.walk(path5[i]):
			for file in dirs:
				if file == var_name:
					path6.append(os.path.join(subdir,file))
					print('Level 5:')
					print(path6)
					break
	path7 = []
	for i in range(0,len(path6)):
		for subdir,dirs,files in os.walk(path6[i]):
			for file in dirs:
				if file == 'latest':
					path7.append(os.path.join(subdir,file))
					print('Level 6:')
					print(path7)
## Construct the final path
	fpath=[]
	for i in range(0,len(path7)):
		for subdir,dirs,files in os.walk(path7[i]):
			for file in files:
				fpath.append(os.path.join(subdir,file))
	return(fpath)	
