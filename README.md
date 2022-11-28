# Project 1: What is the transient sea level sensitivity in CMIP6 models?

Many will be familiar with the concept of transient climate sensitivity: what is the transient temperature response to a doubling in CO2 concentrations? This is a key question for understanding the response of the climate system to CO2 forcing. But there are other important transient responses we need to understand. One of these is the response of global mean sea level to CO2 forcing, which we can call the Transient Sea Level Sensitivity (TSLS). Sea level rise is one of the most serious consequences of climate warming but making projections of it has proved challenging. The TSLS will depend on the coupled climate system response and how glaciers and ice sheets respond to atmospheric and oceanic changes. The aim of this project is to determine the TSLS of CMIP6 coupled models for the 21st century and to compare this to the TSLS that has been estimated for CMIP5 and previous IPCC class experiments in Grinsted and Christensen 2021. This will be achieved by determining the mean response of the oceans and land ice to a change in temperature averaged over multiple decades. We will also explore the spread in TSLS amongst model simulations and the level of confidence we have in the ensemble mean.

# Paper

The project resulted in this paper:

Grinsted, A., Bamber, J., Bingham, R., Buzzard, S., Nias, I., Ng, K., & Weeks, J. (2022). The transient sea level response to external forcing in CMIP6 models. Earth's Future, 10, e2022EF002696. [doi:10.1029/2022EF002696](https://doi.org/10.1029/2022EF002696)

## Plain Language Summary

The planet is warming, and sea levels are rising as oceans expand and ice on land melts. The warmer the Earth gets, the faster the seas will rise. Projecting future sea level rise (SLR) using numerical models has proved extremely challenging and, as a consequence, estimates carry a large uncertainty. How good are the models of ocean expansion and mass loss from glaciers and ice sheets? We tackle this question by comparing how the models react to future warming with how sea level reacted in the past. The models for glaciers, Greenland, and the oceans are compatible with observations. For the largest ice mass on the planet, the Antarctic Ice Sheet, the models do not agree with the observations. As a result, projections of global SLR may be an underestimate.




## Contributors

* Jonathan Bamber, University of Bristol
* Rory Bingham, University of Bristol
* Sammie Buzzard, Cardiff University
* Aslak Grinsted, University of Copenhagen
* Kelvin Ng, University of Birmingham
* Isabel Nias, University of Liverpool
* Jennifer Weeks, Met Office

## What was done

### How we approached the problem and why

As shown in Figure 2 of Grinsted and Christensen (2021), the transient sea level response of the AR5 and SCROCC projections indicate a lower sensitivity to temperature change compared to observations. The overall aim of our project is to update this figure with CMIP6 model results, including the use of ice sheet model projections produced by ISMIP6. We want to explore the major components of the global mean sea level budget (e.g. ice sheets, glaciers, steric) separately to see if they respond differently to rising temperatures.

### Data we used and how to obtain this

* CMIP6 steric sea surface height (calculated by Rory Bingham)
* ISMIP6 emulator data (Edwards et al., 2021): sea level projections from ice sheets, glaciers and ice caps 
* ISMIP6 CMIP6 data (Payne et al., 2021): sea level projections from ice sheets
* CMIP6 global mean surface air temperature

### What we did during the hackathon

* Calculated median sea level response from Greenland, WAIS, EAIS, and Glacier/Ice caps for range of ssp, over two time periods (2016-2050 and 2051-2100), using the ISMIP6 emulator data. Calculated corresponding changes in global surface air temperature.
* Calculated median sea level response from Greenland and Antarctica from ISMIP6 CMIP6 simulations
* Explored the steric sea level response from CMIP6 models over the historical period

### Outcomes

* Recreated Figure 2 from Grinsted and Christensen (2021) to include CMIP6 transient sea level sensitivity.
* Created transient sea level sensitivity plots for the various components of the sea level budget separately.

## About this repo

There are further `README` files in key directories.

### How to reproduce our outputs

Follow the processing order in [_readme.txt](https://github.com/cmip6moap/project01/blob/main/code/Aslak/_readme.txt)

Most input data are located in [data/raw_data](https://github.com/cmip6moap/project01/tree/main/data/raw_data) 

Generated data including intermediate data files are located in [data/processed_data](https://github.com/cmip6moap/project01/tree/main/data/processed_data) 


## Next steps for our project

* Investigate the steric sea level response further and select the best performing ensemble members.
* Explore the components of ice sheet mass balance in more detail. We think the Antarctic response may be due to the complicated relationship between ssp, surface mass balance and ice dynamics. This will involve going back to the ISMIP6 output reported in Seroussi et al. (2020).
* Test sensivity to different time periods.
* Can we go beyond 2100? This will be when the (West) Antarctic response is likely to get very interesting.
