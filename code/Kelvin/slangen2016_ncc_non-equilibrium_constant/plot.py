import csv
import numpy as np
import matplotlib.pyplot as plt
import array
import pandas as pd
from scipy import stats

## INPUT
## Baseline years
ybl_st = 1992
ybl_ed = 2014

## Target range
yta_st = 1970
yta_ed = 2005


odata = pd.read_csv('raw_stat.csv')



Qold = (odata.groupby(by=["model","model_p","model_f","num_nan"]).agg({"odm": "median", "grad": "median"}, as_index=False)).reset_index()

Q = Qold.loc[Qold['num_nan']==0]    ## Only keep entries with no nan
## STANDARD stuff
print(Q)
Q.to_csv('collective_stats.csv',mode='a',sep=',',index=False)
plot = plt.scatter(Q.grad,Q.odm,color="r")
plt.xlabel("Linear residual trend (mm/year)")
plt.ylabel("Mean Obs - Mean Model (mm)") 
plt.axhline(y=0,color="black")
slope,intercept, r, p, se = stats.linregress(Q.grad,Q.odm)
xa = -0.3
ya = -0.3*slope + intercept
xb = 1.5
yb = 1.5*slope+intercept
plt.axline((xa,ya),(xb,yb),color='r',linestyle='--')
#plt.savefig("plot_with_reg.jpeg")
xintercept = -1 * intercept / slope
slope_all = slope
xintercept_all = xintercept
print(xintercept)


## Resampling
flag = 0
for i in range(0,1000):
    Qsample = Q.sample(33)  ## Random sample 75% from the pool
    slope,intercept, r, p, se = stats.linregress(Qsample.grad,Qsample.odm) 
    xint_tmp = -1 * intercept / slope
    if flag == 0:
        grad_sample = slope
        xint_sample = xint_tmp
        flag = 1
    else:
        grad_sample = np.append(grad_sample,slope)
        xint_sample = np.append(xint_sample,xint_tmp)

xint_sample_25 = np.percentile(xint_sample,25)
xint_sample_50 = np.percentile(xint_sample,50)
xint_sample_75 = np.percentile(xint_sample,75)
print(str(xint_sample_25),str(xint_sample_50),str(xint_sample_75))

plt.axvline(x=xintercept_all,color="green")
plt.axvline(x=xint_sample_25,color="blue")
plt.axvline(x=xint_sample_50,color="blue")
plt.axvline(x=xint_sample_75,color="blue")


plt.savefig("plot_with_reg.jpeg")



output_pd = {'x-intercept_all_data':xintercept_all,
        'x-intercept_sample_median':xint_sample_50,
        'x-intercept_sample_lower_quart':xint_sample_25,
        'x-intercept_sample_upper_quart':xint_sample_75}

output_fin = pd.DataFrame(output_pd,index=[0])
output_fin.to_csv('random_sample_stat_for_x-int.csv',mode='a',sep=",",index=False)


