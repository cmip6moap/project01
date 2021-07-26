#!/bin/bash

module load jaspy

mip=("CMIP" "ScenarioMIP" "ScenarioMIP" "ScenarioMIP")
experiment=("historical" "ssp126" "ssp245" "ssp585")
n_model=(135 83 72 69)

n_mip=${#mip[@]}

for (( i=1; i<${n_mip}; i++ ))
do
	echo ${mip[${i}]} ${experiment[${i}]} ${n_model[${i}]}
	mkdir -p ${experiment[${i}]}

#	for (( j=0; j<${n_model[${i}]}; j++ ))
#	do
	for (( j=0; j<${n_model[${i}]}; j++ ))
	do
	echo ${j} ${mip[${i}]} ${experiment[${i}]} ${n_model[${i}]}
		python calc_gmtmp_core.py ${j} ${mip[${i}]} ${experiment[${i}]} 
	done
done
