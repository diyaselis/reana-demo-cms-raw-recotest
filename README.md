REANA Example - Reprocessing AOD from 2010-2012 RAW samples
===========================================================


About
=====
This repository provides an example for the [REANA](http://reanahub.io/) 
reusable research data analysis plaftorm. The objective is to compare the outputs of 
reprocessed AOD files for 2010-2012 RAW samples with CMS Open Data VM results.

Analysis structure
==================

Making a research data analysis reproducible basically means to provide
"runnable recipes" addressing (1) where is the input data, (2) what software was
used to analyse the data, (3) which computing environments were used to run the
software and (4) which computational workflow steps were taken to run the
analysis. This will permit to instantiate the analysis on the computational
cloud and run the analysis to obtain (5) output results.


### 1. Input data

The analysis takes the following inputs:

- the list of RAW samples of corresponding to the existing CMS AODs
