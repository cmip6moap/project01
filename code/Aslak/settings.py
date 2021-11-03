# -*- coding: utf-8 -*-

import numpy as np
import os
import colorsys


#some colormaps...
#categorical
sashamap99 = ['#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#42d4f4', '#f032e6', '#fabed4', #0-7
              '#469990', '#dcbeff', '#9A6324', '#fffac8', '#800000', '#aaffc3', '#000075', '#a9a9a9', #8-15
              '#ffffff', '#000000'] #https://sashamaps.net/docs/resources/20-colors/  -99%accessibility!
tol = ["#332288","#117733","#44AA99","#88CCEE","#DDCC77","#CC6677","#AA4499","#882255"] #paul-tol-2011
tol_muted = ["#CC6677","#332288","#DDCC77","#117733","#88CCEE","#882255","#44AA99","#999933","#AA4499","#DDDDDD","#000000"]
tol_medium = ["#6699CC","#004488","#EECC66","#994455","#997700","#EE99AA","#000000"]
tol_bright = ["#4477AA","#EE6677","#228833","#CCBB44","#66CCEE","#AA3377","#BBBBBB","#000000"]
tol_pale = ["#BBCCEE","#FFCCCC","#CCDDAA","#EEEEBB","#CCEEFF","#DDDDDD","#000000"]
wong2011 = ["#000000","#0072B2","#56B4E9","#009E73","#F0E442","#E69F00","#D55E00","#CC79A7"]
ibm_plus_one = ["#648FFF","#FFB000","#FE6100","#DC267F","#785EF0","#312A58"] #ibm+1

#sequential....
#Ideally not vary strongly intensity - so rainbow like but colorblind friendly...)
traffic_light = [sashamap99[ix] for ix in [17,10,3,8,1,2,4,0]]
tol_rainbow_discrete22 = ['#6F4C9B', '#6059A9', '#5568B8', '#4E79C5', '#4D8AC6',
                '#4E96BC', '#549EB3', '#59A5A9', '#60AB9E', '#69B190',
                '#77B77D', '#8CBC68', '#A6BE54', '#BEBC48', '#D1B541',
                '#DDAA3C', '#E49C39', '#E78C35', '#E67932', '#E4632D',
                '#DF4828', '#DA2222'] #paultol discrete rainbow22
AR6_scenarios_colors = ['#B3AA96',"000000","#00a9cf","#003466","#f69320","#df0000","#980002"] #with 2 colors pre-pended

#select two colormaps... for scatter plots and TSLS
#sequential_colormap = tol_rainbow_discrete22[0::3]
sequential_colormap = AR6_scenarios_colors
categorical_colormap = tol_bright


#we want a consistent set of colors for the different plots. So i've made that a setting...
scenariocolors = {
    "SSP119": sequential_colormap[-5],
    "SSP126": sequential_colormap[-4],
    "SSP245": sequential_colormap[-3],
    "SSP370": sequential_colormap[-2],
    "SSP585": sequential_colormap[-1],
    "SSPNDC": '#a9a9a9',
    "HISTORICAL": sequential_colormap[0]
}

targetperiods = np.array([[1850,1900],[1900,1950],[1950,2000],[1992,2014],
                          [2016,2050],[2051,2100]])


periodcolors = {"historical": categorical_colormap[2],
                "experts": categorical_colormap[0],
                "observations": categorical_colormap[1],
                "2016-2050": categorical_colormap[4],
                "2051-2100": categorical_colormap[5],
                "1850-2014": categorical_colormap[3], #THIS ONE IS USED IN TSLS
                #NOT USED from here?
                "1850-1900": scenariocolors['HISTORICAL'],
                "1900-1950": scenariocolors['HISTORICAL'],
                "1992-2014": scenariocolors['HISTORICAL'],
}


baseline_period = [1995,2014]


eflag = 1



datafolder = os.path.abspath('../../data')


if __name__ == "__main__":
    # this is some test code:
    import matplotlib.pyplot as plt
    x = np.arange(len(categorical_colormap))
    plt.scatter(x,x*0,c=categorical_colormap,marker='o',s=200)
    for xx in x:
        plt.text(xx,0,f'{xx}',horizontalalignment='center',verticalalignment='center')

    x = np.arange(len(sequential_colormap))
    plt.scatter(x,x*0-1,c=sequential_colormap,marker='o',s=200)
    for xx in x:
        plt.text(xx,0-1,f'{xx}',horizontalalignment='center',verticalalignment='center')


    row = 2
    for k,v in scenariocolors.items():
        plt.plot(0,row,'.',color=v,markersize=30)
        plt.text(0,row,f'  {k}',verticalalignment='center')
        row= row+1

    row = 2
    for k,v in periodcolors.items():
        plt.plot(5,row,'.',color=v,markersize=30)
        plt.text(5,row,f'  {k}',verticalalignment='center')
        row= row+1


