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

2010 Selected RAW files:

•	/MinimumBias/Run2010B-Apr21ReReco-v1/RAW 
•	/Mu/Run2010B-Apr21ReReco-v1/RAW 
•	/Electron/Run2010B-Apr21ReReco-v1/RAW 
•	/Jet/Run2010B-Apr21ReReco-v1/RAW 

2011 Selected RAW files:

•	/SingleMu/Run2011A-12Oct2013-v1/RAW 
•	/SingleElectron/Run2011A-12Oct2013-v1/RAW 
•	/DoubleElectron/Run2011A-12Oct2013-v1/RAW
•	/DoubleMu/Run2011A-12Oct2013-v1/RAW
•	/Jet/Run2011A-12Oct2013-v1/RAW 

2012 Selected RAW files:

•	/MinimumBias/Run2012B-22Jan2013-v1/RAW 
•	/SingleMu/Run2012B-22Jan2013-v1/RAW 
•	/SingleElectron/Run2012B-22Jan2013-v1/RAW 
•	/DoubleMuParked/Run2012B-22Jan2013-v1/RAW 
•	/DoubleElectron/Run2012B-22Jan2013-v1/RAW 
•	/JetHT/Run2012B-22Jan2013-v1/RAW 

Analysis structure
==================

.. code-block:: console

cmsrel CMSSW_5_3_32
cd CMSSW_5_3_32/src
cmsenv
mkdir WorkDir
cd WorkDir
git clone git://github.com/cms-opendata-validation/recotest.git

cd recotest
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA FT_53_LV5_AN1
ln -sf /cvmfs/cms-opendata-conddb.cern.ch/FT_53_LV5_AN1_RUNA.db FT_53_LV5_AN1_RUNA.db
ls -l
ls -l /cvmfs/
cmsRun configFile.py

