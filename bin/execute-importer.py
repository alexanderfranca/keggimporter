import sys
import os
sys.path.insert(0,  os.getcwd() + '/../keggimporter')

import logging
import logging.handlers
from Config import *
from Importer import *

config = Config()
config.loadConfiguration()
conf = config.getConfigurations()

logFile = conf.get( 'log', 'info' )

log = logging.getLogger('')
log.setLevel(logging.DEBUG)
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(format)
log.addHandler(ch)

fh = logging.handlers.RotatingFileHandler( logFile , maxBytes=0, backupCount=0)
fh.setFormatter(format)
log.addHandler(fh)


log.info('keggimporter: START')

imp = Importer()

imp.startImporter()

log.info('writeTaxonomies: START')
imp.writeTaxonomies()
log.info('writeTaxonomies: DONE')

log.info('writePathways: START')
imp.writePathways()
log.info('writePathways: DONE')

log.info('writeEcs: START')
imp.writeEcs()
log.info('writeEcs: DONE')

log.info('writeOrganisms: START')
imp.writeOrganisms()
log.info('writeOrganisms: DONE')

log.info('writeProteins: START')
imp.writeProteins()
log.info('writeProteins: DONE')

log.info('writeProteinRelations: START')
imp.writeProteinRelations()
log.info('writeProteinRelations: DONE')

log.info('writeOrganismTaxonomies: START')
imp.writeOrganismTaxonomies()
log.info('writeOrganismTaxonomies: DONE')

log.info('writeProteinAccessions: START')
imp.writeProteinAccessions()
log.info('writeProteinAccessions: DONE')

log.info('writeEcMaps: START')
imp.writeEcMaps()
log.info('writeEcMaps: DONE')

log.info('keggimporter: DONE')


