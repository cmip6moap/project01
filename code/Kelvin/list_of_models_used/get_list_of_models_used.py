# -*- coding: utf-8 -*-

import numpy as np
from glob import glob
import pandas as pd
import re


'''
alist.sort(key=natural_keys) sorts in human order
http://nedbatchelder.com/blog/200712/human_sorting.html
(See Toothy's implementation in the comments)
'''

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


datafolder = "../../../data"

steric = pd.read_csv(f'{datafolder}/processed_data/ExtractedFromSSH/StericTvsRate_individualruns.csv')

tmp = steric.run
new_tmp = [s.split('_')[0] for s in tmp]    ## Remove the _gn/_gr
steric.run = new_tmp                        ## Update run

#get_r = [(s.split('i')[0]).strip('r') for s in new_tmp] ## Get r value
#steric['r'] = get_r
groups = steric.groupby(['scenario','model'])

output = []

for name, group in groups:
    vlist = sorted(set(group.run),key=natural_keys)
    flag = 0
    for v in vlist:
        if flag == 0:
            v_fin = v
            flag = 1
        else:
            v_fin = v_fin+"/"+v ## Separator is "/"
    newrow={"model":name[1],
            "scenario":name[0],
            "variant":v_fin}
    output.append(newrow)

output = pd.DataFrame(output)
fout = f'./list_of_model_variants_used.csv'
output.to_csv(fout)
