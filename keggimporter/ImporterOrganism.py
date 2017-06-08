import pprint
from keggreader import *
from Config import *
import sys

class ImporterOrganism:

    def __init__( self ):

        self.organismPrimaryKey = 0
        self.organismsInserted  = {}


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


    def openOrganismsFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'organismsInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def nextOrganismPrimaryKey( self ):
        """
        Controls the organisms table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.organismPrimaryKey += 1

        return self.organismPrimaryKey


    def writeOrganismsFile( self, organism_file=None, organism_code=None, organism_kegg_name=None, organism_internal_kegg_id=None, taxonomy_id=None ):
        """
        Actual write the organisms inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextOrganismPrimaryKey()

        organism_file.write( str(nextId) + '\t' + str(organism_code) + '\t' + str(organism_kegg_name) + '\t' + str(organism_internal_kegg_id) + '\t' + str( taxonomy_id ) + "\n" )

        self.organismsInserted[ str( organism_code ) ] = nextId 


    def writeOrganisms( self ):
        """
        Write the organisms insert file.
        """

        organismsDestination = self.openOrganismsFile()

        organisms = self.reader.getAllOrganisms() 
        
        for organismCode,organismData in organisms.iteritems():
            self.writeOrganismsFile( organismsDestination,  organismCode, organismData['genome']['kegg_definition_name'], organismData['genome']['kegg_organism_id'], organismData['genome']['taxonomy_id'] )





