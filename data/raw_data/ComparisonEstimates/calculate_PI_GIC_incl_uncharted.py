# -*- coding: utf-8 -*-



import numpy as np


#Marzeion 2015 estimate for 1850-1900: (updated leclercq 2011)
M15 = 0.434
M15sigma = 0.11

#from figure 2 we see that 25%-50% percent
PM18 = np.array([.25, .5])

multiplier = 1/(1-PM18)

log_multiplier_mu = np.mean(np.log(multiplier))

# interpret range as \pm2\sigma
log_multiplier_sigma = np.diff(np.log(multiplier))[0]/4


V = np.empty(10000)
for ii in range(len(V)):
    v = M15 + np.random.randn()*M15sigma
    m = np.exp(log_multiplier_mu + np.random.randn()*log_multiplier_sigma)
    V[ii] = v*m


print(f'GIC 1850-1900: {np.mean(V):.2f} \pm {np.std(V):.2f}')