#!/bin/bash

module purge
module load bluebear
module load Python/3.7.2-GCCcore-8.2.0
module load scikit-learn/0.21.3-foss-2019a-Python-3.7.2
python calc_tmp.py
