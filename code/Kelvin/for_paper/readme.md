This directory includes some modified scripts based on Aslak's scripts.

Update: 21 Oct 2021
tas_tools_v2.py:

	--> If the target TAS file is NOT found in the directory 

		'raw_data/cmip6_tas_for_steric_analysis'

		It will search the other direcotry as well

		'raw_data/cmip6_tas_for_steric_analysis_all_JASMIN'

steric_tools_v2.py:

	--> It reads the variable 'datafolder' from setting_v2.py

		Just for convenience

settings_v2.py:

	--> Added variable
		
		==> outputfolder : to store the output

		==> eflag : Flag to control whether error message should be printed or not


extract_steric_v2.py

	--> Baseline historical TAS will be calculated if steric timeseries (any scenario) exists
