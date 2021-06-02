import csv
import numpy as np
import matplotlib.pyplot as plt
import array

mip = "ScenarioMIP"
expr = "ssp126"
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
