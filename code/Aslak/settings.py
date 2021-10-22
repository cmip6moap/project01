# -*- coding: utf-8 -*-

import numpy as np
import os
import colorsys



distinctcolors = ['#e6194B', '#3cb44b', '#ffe119','#4363d8', '#f58231',
                  '#42d4f4', '#f032e6', '#fabebe', '#469990', '#e6beff',
                  '#9A6324', '#fffac8', '#800000', '#aaffc3', '#000075',
                  '#a9a9a9', '#ffffff', '#000000']





#we want a consistent set of colors for the different plots. So i've made that a setting...
scenariocolors = {
    "SSP119": distinctcolors[8],
    "SSP126": distinctcolors[1],
    "SSP245": distinctcolors[2],
    "SSP370": distinctcolors[4],
    "SSP585": distinctcolors[0],
    "SSPNDC": distinctcolors[15],
    "HISTORICAL": distinctcolors[10]
}

targetperiods = np.array([[1850,1900],[1900,1950],[1950,2000],[1992,2014],
                          [2016,2050],[2051,2100]])

periodcolors = {"historical": distinctcolors[10],
                "experts": distinctcolors[9],
                "observations": '#888888',
                "1850-2014": distinctcolors[10],
                "1850-1900": distinctcolors[10],
                "1900-1950": distinctcolors[10],
                "1992-2014": distinctcolors[10],
                "2016-2050": distinctcolors[5],
                "2051-2100": distinctcolors[3]}


baseline_period = [1995,2014]


eflag = 1



datafolder = os.path.abspath('../../data')


if __name__ == "__main__":
    # this is some test code:
    import matplotlib.pyplot as plt
    x = np.arange(len(distinctcolors))
    plt.scatter(x,x*0,c=distinctcolors,marker='o')
    for xx in x:
        plt.text(xx,0,f'{xx}')


