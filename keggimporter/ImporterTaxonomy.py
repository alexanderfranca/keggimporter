import pprint
from keggreader import *
from Config import *
import sys

class ImporterTaxonomy:

    def __init__( self ):

        self.taxonomyPrimaryKey = 0
        self.taxonomiesInserted  = {}


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


    def openTaxonomiesFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'taxonomiesInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def nextTaxonomyPrimaryKey( self ):
        """
        Controls the taxonomies table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.taxonomyPrimaryKey += 1

        return self.taxonomyPrimaryKey


    def writeTaxonomiesFile( self, taxonomy_file=None, name=None, tax_id=None, tax_type=None ):
        """
        Actual write the taxonomies inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextTaxonomyPrimaryKey()

        taxonomy_file.write( str(nextId) + '\t' + str(name) + '\t' + str(tax_id) + '\t' + str(tax_type) + "\n" )

        self.taxonomiesInserted[ str( name ) ] = nextId 


    def writeTaxonomies( self ):
        """
        Write the taxonomies insert file.
        """

        taxonomies = {}

        taxonomiesDestination = self.openTaxonomiesFile()

        organisms = self.reader.getAllOrganisms() 
        
        for organismCode,organismData in organisms.iteritems():
            for lineage in organismData['lineage']:

                taxonomies[ lineage['name'] ] = { 'name': lineage['name'], 'tax_id': lineage['tax_id'], 'type': lineage['type'] }



        for tax,data in taxonomies.iteritems():
            #pprint.pprint( data )
            self.writeTaxonomiesFile( taxonomiesDestination,  data['name'], data['tax_id'], data['type'] )




