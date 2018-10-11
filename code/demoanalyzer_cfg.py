import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

# initialize MessageLogger and output report
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'
process.MessageLogger.categories.append('Demo')
process.MessageLogger.cerr.INFO = cms.untracked.PSet(
        limit = cms.untracked.int32(-1)
        )
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True), 
										SkipEvent = cms.untracked.vstring('ProductNotFound')
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(20000) )

process.source = cms.Source("PoolSource",
                                # replace 'myfile.root' with the source file you want to use
                                fileNames = cms.untracked.vstring(

          'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/MinimumBias/AOD/12Oct2013-v1/00000/0A299FE5-7B46-E311-87C7-0025901AF1C6.root',
        'root://eospublic.cern.ch//eos/opendata/cms/Run2011A/MinimumBias/AOD/12Oct2013-v1/00000/D2235F26-7C46-E311-86E4-0025904B2294.root'

#       'file:rereco22524.root'
                ),
                          lumisToProcess = cms.untracked.VLuminosityBlockRange('160957:910-160957:max')
                            #firstRun = cms.untracked.uint32(169957),
                            #firstEvent = cms.untracked.uint32(488034889)
                            )

process.demo = cms.EDAnalyzer('PhysicsObjectsHistos',

                                         minTracks=cms.untracked.uint32(0)
                              )

process.TFileService = cms.Service("TFileService",
                                       fileName = cms.string('histodemo.root')
                                   )


process.p = cms.Path(process.demo)
