import sys
import os
sys.path.insert(0,  os.getcwd() + '/../keggimporter')

import logging
import logging.handlers
from Config import *
from Loader import *

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


log.info('loader: START')

ld = Loader()
ld.start()

if ld.checkPsqlCanExecuteCommand():
	log.info('loader: psql available.' )
else:
	log.info('ERROR: psql command is NOT AVAILABLE.' )
	sys.exit()


if ld.checkYouHaveTheRightTables():
	log.info('loader: your tables are correct.' )
else:
	log.info('ERROR: your database tables are wrong.')
	sys.exit()


log.info('loader: all checks are ok.')

log.info('loader: start loading insert files to the relational database tables.')

ld.loadFiles()

log.info('loader: DONE.')

