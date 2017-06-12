import pprint
from keggreader import *
from Config import *
import sys

class ImporterEc:

    def __init__( self ):

        self.ecPrimaryKey = 0
        self.ecsInserted  = {}

        self.reader = KeggReader()
        self.config = Config()
        self.afs    = AnendbFileSystem()

        self.config.loadConfiguration()
        self.conf = self.config.getConfigurations()


    def startImporter( self ):

        self.reader = KeggReader()
        self.config = Config()
        self.afs    = AnendbFileSystem()

        self.config.loadConfiguration()
        self.conf = self.config.getConfigurations()


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


    def openEcsFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'ecsInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def nextEcPrimaryKey( self ):
        """
        Controls the ecs table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.ecPrimaryKey += 1

        return self.ecPrimaryKey


    def writeEcsFile( self, ec_file=None, ec=None ):
        """
        Actual write the ecs inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextEcPrimaryKey()

        ec_file.write( str(nextId) + '\t' + str(ec) + "\n" )

        self.ecsInserted[ str( ec ) ] = nextId 


    def writeEcs( self ):
        """
        Write the ecs insert file.
        """

        ecsDestination = self.openEcsFile()

        ecs = self.reader.getAllEcNumbers() 
        
        for ec in ecs:
            self.writeEcsFile( ecsDestination, ec )





