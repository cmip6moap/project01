# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:46:09 2021

@author: ag
"""



#This script runs everything in the right order.

#1) configure paths etc in settings.py
import extract_steric
import extract_iceemu
import combine_v2

import extract_iceemu_sensitivity
import extract_steric_sensitivity
import extract_comparison_estimates


import fig_ice_scatter
import fig_steric_scatter
import fig_gmsl_scatter


import fig_tsls_histograms
