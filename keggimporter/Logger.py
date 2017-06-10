import pprint
from Config import *
import sys
import logging
import logging.handlers

class Logger:
    """
    Provides a logging system.
    """

    def __init__( self ):

        self.config = Config()

        self.config.loadConfiguration()
        self.conf = self.config.getConfigurations()


    def createLogSystem(self):
        """
        Set all logger parameters (file log path, for example), output format and set the class property that stores the logging system.

        """

        logFile  = self.getConfiguration( 'log', 'info' )

        log = logging.getLogger('')
        log.setLevel(logging.DEBUG)
        format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(format)
        log.addHandler(ch)

        fh = logging.handlers.RotatingFileHandler( logFile , maxBytes=0, backupCount=0)
        fh.setFormatter(format)
        log.addHandler(fh)

        return log


    def getConfiguration( self, section=None, option=None ):
        """
        Load the configurations from configuration file.

        Returns configurations found in the keggimporter.conf file.

        Args:
            section(str): Section form keggimporter.conf file.
            option(str): What option to read from keggimporter.conf file.

        Returns:
            (str): Configuration value from the keggimporter.conf file, in the spe
        """

        return self.conf.get( section, option )


    def setConfigurationFile( self, conf_file=None ):
        """
        Set the current keggimporter.conf file.

        Args:
            conf_file(str): Full path for the keggimporter.conf
        
        """

        self.config.configurationFile = conf_file
        self.config.loadConfiguration()
        self.conf = self.config.getConfigurations()



