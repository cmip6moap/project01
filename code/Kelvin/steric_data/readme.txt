Script:

#####################################################

INPUT:

ybl_st = beginning of the baseline years [inclusive], current: 1992
ybl_ed = end of the baseline years [inclusive], current: 2014

yta_st = beginning of the target range [inclusive], current: 1970
yta_ed = end of the target range [inclusive], current: 2005

#####################################################

OUTPUT:

model = Model name

run = run

lin_grad = slope steric model vs time (linear regression)

r = pearson's r

p = p-value of pearson's r

mean_omm = Average difference between obs and model [FigS2 of Slangen et al 2016, y-axis]

resid_grad = Gradient of residual [FigS2 of Slangen et al 2016, x-axis]

ks_stat = Kolmogorov-Smirnov statistic on 2 samples

ks_pval = p-value of ks_stat
