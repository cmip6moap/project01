Steric SSH time series from CMIP6 runs.

Monthly mean timeseries computed from the potential temperature and salinity CMIP6 output or obtained from zostoga variable.

Historical and SSP timeseries have been screened for obviously bad timeseries and duplicates (same run on more than one grid, in which case the native grid is used) and zostoga has been used where it is available but a direct steric calculation has not been possible. 

Notes

  Historical:
   - 135 unique runs; 131 steric gm; 4 zostoga
   - CNRM-CM6-1 (runs 53-62) and CNRM-ESM2-1 (runs 63-66) only start in Jan 2000
   - FGOALS-f3-L (run 71) bad first value set to zero
   - FGOALS-g3 (run 72) bad first value set to zero
   - INM-CM5-0 (run 97) bad value at Dec 1938 set to average of surrounding values
   - historical zostoga available for NorCPM1 but only starts in Jan 2015 so not included 
   - Outlier models: FGOALS-g3 (runs 71), INM-CM4-8 (run 96) and INM-CM5-0 (run 71) monotonic decline throughout historical period
                     UKESM1-0-LL (particularly runs 116-118 and 122) general decline until ~2000 

  SSP126:
   - 83 unique runs; 77 steric gm; 6 zostoga
   - CMCC-CM2-SR5 (run 32) incomplete
   - FGOALS-f3-L (runs 37-39) bad first value set to zero 
   - FGOALS-g3 (runs 40, 42) bad first value set to zero 
   - MRI-ESM2-0 (run 63) discontinuity at 2100 fixed by removing offset
   - Outlier models: FGOALS-g3 (runs 40-42), INM-CM4-8 (run 49) and INM-CM5-0 (run 50) 

  SSP245:
   - 72 unique runs; 62 steric gm; 10 zostoga
   - 3 runs of HadGEM3-GC-LL (runs 44-46) end in Dec 2020
   - FGOALS-g3 (run 39) bad first value set to zero

  SSP585:
   - 69 unique runs; 63 steric gm; 6 zostoga
   - E3M-1-1 (run 31) ends in Dec 2019
   - CIESM (run 28) bad first value set to zero
   - FGOALS-f3-L (run 36) bad first value set to zero
   - FGOALS-g3 (run 37) bad first value set to zero
    
   Even though potential temperature and salinity fields are available and the steric calculation does not crash the bad steric values are produced for the following models (will investigate futher):
   - CESM2 (-FV2, -WACCM, -WACCM-FV2)
   - CMCC-CM2-HR4
   - E3SM-1-0
   - GISS-E2-1-H
   - KIOST-ESM
   - MIROC6; MIROC-ES2L
   - MRI-ESM2-0
   - NorESM2-LM (-MM); NorCPM1
