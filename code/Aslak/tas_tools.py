"""

This script contains helper functions for reading the TAS files in
https://github.com/cmip6moap/project01/tree/main/data/raw_data/cmip6_tas_for_steric_analysis

Aslak Grinsted 2021 during CMIP6moap

Modified by Kelvin Ng 2021 Oct

"""



import numpy as np
import pandas as pd
import re
import os.path
from settings import datafolder, eflag


def parse_run(run):
    r = re.findall('r(\d+|ave)', run)
    if r is None:
        r = re.findall(r'_(\d+|ave)$', run)
    if r:
        r = r[0][0]
    else:
        r = 'ave'
    i = re.findall(r'i(\d+)', run)[0][0]
    p = re.findall(r'p(\d+)', run)[0][0]
    f = re.findall(r'f(\d+)', run)[0][0]
    return r,i,p,f


def load_tas(model= 'ACCESS-CM2', scenario='historical', run='r1i1p1f1_gn', return_annual=True):
    if scenario == 'historical':
        mip = 'CMIP'
    else:
        mip = 'ScenarioMIP'

    filename = f'{datafolder}/raw_data/cmip6_tas_for_steric_analysis/{scenario}/gm_tas_{mip}_{scenario}_{model}_{run}.csv'

    if not os.path.isfile(filename):
        ## Try another path if the default one does not have our file
        filename = f'{datafolder}/raw_data/cmip6_tas_for_steric_analysis_all_JASMIN/{scenario}/gm_tas_{mip}_{scenario}_{model}_{run}.csv'
        if not os.path.isfile(filename):
            if eflag == 1:
                print(f'file not found: {filename}')
            return None
    df = pd.read_csv(filename)
    df.gm_tas.replace({0: np.nan})
    df['month'] = df.time % 100
    df['year'] = ((df.time-df.month)/100).astype(int)
    if return_annual:
        return df.groupby('year').agg({'gm_tas': 'mean'})
    return df

if __name__ == "__main__":
    # this is some test code:
    d = load_tas()
    import matplotlib.pyplot as plt
    plt.plot(d)
