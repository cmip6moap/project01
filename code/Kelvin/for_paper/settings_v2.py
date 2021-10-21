# -*- coding: utf-8 -*-

import numpy as np
import os

distinctcolors = ['#e6194B', '#3cb44b', '#ffe119','#4363d8', '#f58231',
                  '#42d4f4', '#f032e6', '#fabebe', '#469990', '#e6beff',
                  '#9A6324', '#fffac8', '#800000', '#aaffc3', '#000075',
                  '#a9a9a9', '#ffffff', '#000000']

#we want a consistent set of colors for the different plots. So i've made that a setting...
scenariocolors = {
    "SSP119": distinctcolors[0],
    "SSP126": distinctcolors[1],
    "SSP245": distinctcolors[2],
    "SSP370": distinctcolors[3],
    "SSP585": distinctcolors[4],
    "SSPNDC": distinctcolors[5],
    "HISTORICAL": distinctcolors[6]
}

# Original target periods
targetperiods = np.array([[1850,1900],[1900,1950],[1950,2000],[1992,2014],
                          [2016,2050],[2051,2100]])

# Original period colors
periodcolors = {"historical": distinctcolors[6],
                "1850-2014": distinctcolors[6],
                "1850-1900": distinctcolors[6],
                "1900-1950": distinctcolors[6],
                "1992-2014": distinctcolors[6],
                "2016-2050": distinctcolors[7],
                "2051-2100": distinctcolors[8]}

baseline_period = [1995,2014]




## NAMELIST
## ROOT path to data files
datafolder = os.path.abspath('/rds/projects/l/leckebgc-pre-cax/ngks/cop26_bristol/project01/data')

## Path to the output folder
outputfolder = os.path.abspath('/rds/projects/l/leckebgc-pre-cax/ngks/cop26_bristol/mywork/paper/steric/paper_output')

## Flag for error message
##  1 = Print everything
##  0 = Print nothing

eflag = 1

