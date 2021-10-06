# -*- coding: utf-8 -*-

import numpy as np
import os

#we want a consistent set of colors for the different plots. So i've made that a setting...
scenariocolors = {
    "SSP119": "#e6194B",
    "SSP126": "#3cb44b",
    "SSP245": "#ffe119",
    "SSP370": "#4363d8",
    "SSP585": "#f58231",
    "SSPNDC": "#42d4f4",
    "HISTORICAL": "#f032e6"
}

targetperiods = np.array([[1850,1900],[1900,1950],[1950,2000],[1992,2014],[2016,2050],[2051,2100]])

baseline_period = [1995,2014]



datafolder = os.path.abspath('../../data')


# distinctcolors = ['#e6194B', '#3cb44b', '#ffe119','#4363d8', '#f58231', '#42d4f4', '#f032e6', '#fabebe', '#469990', '#e6beff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#000075', '#a9a9a9', '#ffffff', '#000000']
