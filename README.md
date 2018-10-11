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
	Run Range: [146428,146514] - Number of events: 2451242

•	/Mu/Run2010B-Apr21ReReco-v1/RAW 
	Run Range:  [146589,146710] - Number of events: 2102829

•	/Electron/Run2010B-Apr21ReReco-v1/RAW 
	Run Range: [146712,146804] - Number of events: 2554874

•	/Jet/Run2010B-Apr21ReReco-v1/RAW 
	Run Range: [146807, 147043] - Number of events: 2415753

2011 Selected RAW files:

•	/SingleMu/Run2011A-12Oct2013-v1/RAW 
	Run Range:  [163289,163370] - Number of events: 2079006

•	/SingleElectron/Run2011A-12Oct2013-v1/RAW 
	Run Range: [161224,163286] - Number of events: 2064298

•	/DoubleElectron/Run2011A-12Oct2013-v1/RAW
	Run Range:  [160431,161223] - Number of events: 2035725

•	/DoubleMu/Run2011A-12Oct2013-v1/RAW
	Run Range:  [163371,163588] - Number of events: 2070977

•	/Jet/Run2011A-12Oct2013-v1/RAW 
	Run Range:  [163589,165121] - Number of events: 2177197

2012 Selected RAW files:

•	/MinimumBias/Run2012B-22Jan2013-v1/RAW 
	Run Range:  [193834, 194050] - Number of events: 2745751

•	/SingleMu/Run2012B-22Jan2013-v1/RAW 
	Run Range: [194051,194115] - Number of events: 2301668

•	/SingleElectron/Run2012B-22Jan2013-v1/RAW 
	Run Range: [194117, 194199] - Number of events: 2125485

•	/DoubleMuParked/Run2012B-22Jan2013-v1/RAW 
	Run Range:  [194210,194429] - Number of events: 2047989

•	/DoubleElectron/Run2012B-22Jan2013-v1/RAW 
	Run Range: [194439,194691] - Number of events: 2060895

•	/JetHT/Run2012B-22Jan2013-v1/RAW 
	Run Range: [194699,195112] - Number of events: 2096284


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

