
# I’ve attached a figure with all the time series that went into our estimates. GP = Greenland peripheral glaciers, M&D = Missing & Disappeared glaciers. I’ve also attached a data file with all the trends that I computed over the AR6 periods that also include the uncertainties. It’s a Python/numpy file, and this command should load the file:

import numpy as np
stats = np.load('stats_basin_global.npy',allow_pickle=True).all()

# Then, the trends for observed GMSL are stored as dictionaries within this file. To show all the components, then run:

# stats["global"].keys()

# The observed GMSL trends then show up if you type

# stats["global"]["obs"]

# Which should give the time series and at the end the trends:

# 'trend_1900_2018': array([ 1.5590526 , -0.32608284,  0.32570602]),
# 'trend_1957_2018': array([ 1.77520187, -0.29996452,  0.30013279]),
# 'trend_1993_2018': array([ 3.35012592, -0.46057008,  0.46348239]),
# 'trend_1900_1949': array([ 1.34955675, -0.50915415,  0.50806184]),
# 'trend_1950_1999': array([ 0.98695231, -0.3456766 ,  0.36832388]),
# 'trend_1900_1956': array([ 1.55189052, -0.47334641,  0.46303397]),
# 'trend_1957_1993': array([ 0.87219705, -0.37207373,  0.38602746]),
# 'trend_1901_2018': array([ 1.56653093, -0.32566036,  0.29980854]),
# 'trend_1901_1990': array([ 1.44329056, -0.3724046 ,  0.37391159]),
# 'trend_1971_2018': array([ 2.24392976, -0.30802869,  0.30662267]),
# 'trend_2006_2018': array([ 4.27840446, -1.04768399,  1.09513025])}

# The first number is the mean of the estimate,
# and both numbers give the lower and upper bound relative to the mean.

# The individual components are also there:

stats["global"].keys()
# Out[18]: dict_keys(['obs', 'steric', 'grd_glac', 'grd_GrIS', 'grd_AIS', 'grd_tws', 'grd_total', 'grd_tws_natural', 'grd_tws_gwd', 'grd_tws_dam', 'grd_ice', 'altimetry', 'budget', 'diff', 'obs_steric'])

# stats[“global”][“grd_glac”] is the glacier contribution, grd_GrIS = Greenland, “steric” (not obs_steric) is the steric component etc.

# Hope this helps!

# Cheers,

# Thomas
