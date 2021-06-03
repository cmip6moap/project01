import csv
import numpy as np
import matplotlib.pyplot as plt
import array

scenarios = ['SSP126','SSP245','SSP585']
for scenario in scenarios:

    mip = "ScenarioMIP"
    expr = scenario.lower()
    run_to_plot = 1 # run listed on row of corresponding text file

    yr_strt = 2001
    yr_end = 2310
    n_mnths = 12 * (yr_end - yr_strt + 1)

    yr_ref = 2020
    n_ref = 12 * (yr_ref - yr_strt) + 1

    fn = "cmip6_" + mip + "_" + expr + "_strh_gm.dat"
    print(fn)
    fid = open(fn, mode = 'rb')
    a = array.array("i")
    a.fromfile(fid, 1)

    b = a[0]
    n_vals = b // 4
    n_runs = n_vals // n_mnths
    print(n_runs)

    tmp = array.array("f")
    tmp.fromfile(fid, b//4+1)
    tmp = tmp[1:]
    tmp = np.asarray(tmp)
    strh_gm = np.reshape(tmp, (n_runs, n_mnths), 'F')
    strh_gm[strh_gm==0] = "NaN"
    for i in range(n_runs): # reference to Jan 2020
      strh_gm[i,:] = strh_gm[i,:] - strh_gm[i,n_ref]

    x = np.zeros(n_mnths)
    print(len(x))
    for i in range(n_mnths):
        x[i] = (i + 0.5) / 12 + yr_strt
    plt.plot(x, strh_gm[run_to_plot-1,:])
    plt.xlabel("year")
    plt.ylabel("metres")
    plt.title("Global mean steric height (relative to Jan 2020)")
    plt.show()


    #ASLAKs additions:
    #removes fishy values and saves the data for easier loading later

    #-----------------------
    import pandas as pd
    modelnames = pd.read_csv(f'cmip6_ScenarioMIP_{expr}_strh_gm_run_list.txt', sep = '\s+', names=['no','model','run'], index_col='no')

    t = x
    steric = strh_gm
    steric[-1,-1] = np.nan

    #remove fishy first values:
    for no in range(steric.shape[0]):
        ixfirst = np.argmax(~np.isnan(steric[no,:]))
        if np.abs(steric[no,ixfirst]-steric[no,ixfirst+1])>0.1:
            steric[no,ixfirst] = np.nan

    #remove sudden outliers:
    from scipy.ndimage import median_filter
    m = median_filter(steric,size=(5,1))
    steric = np.where(np.abs(steric-m)>1, m, steric)


    #------------------SAVE IT-------------------


    np.savez(f'{scenario}_cleaned.npz',t, steric, modelnames) # this format is convenient to load in python

    #also save as text file
    headers = modelnames.iloc[:,0:2].agg('/'.join, axis=1).to_list()
    headers.insert(0,'time')

    d=np.append(np.array([t]).T, steric.T, axis=1)

    np.savetxt(f'{scenario}_cleaned.txt', d, header=' '.join(headers) )

