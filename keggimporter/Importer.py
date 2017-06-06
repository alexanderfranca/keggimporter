import pprint
from keggreader import *
from Config import *
from ImporterProtein import *
from ImporterEc import *
import sys

class Importer:

    def __init__( self ):

        self.importerProtein = ImporterProtein()
        self.importerEc      = ImporterEc()
        self.reader          = KeggReader()

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


    def openProteinEcsFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'proteinEcsInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def nextProteinEcsPrimaryKey( self ):
        """
        Controls the proteins table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.proteinEcsPrimaryKey += 1

        return self.proteinEcsPrimaryKey


    def writeProteinEcsFile( self, protein_ecs_file=None, protein_id=None, ec_id=None ):
        """
        Actual write the protein_ecs inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextProteinEcsPrimaryKey()

        protein_ecs_file.write( str(nextId) + '\t' + str(protein_id) + '\t' + str(ec_id) + "\n" )

        #self.proteinEcsInserted[ str(identification ) ] = nextId 
        

    # TODO: test, comments
    def writeProteins( self ): 

        self.importerProtein.writeProteins()
        self.importerEc.writeEcs()

        for protein,databaseId in self.importerProtein.proteinsInserted.iteritems():
            ecs = self.reader.getEcNumberByGene( protein ) 

            if ecs:
                for ec in ecs:
                    #pprint.pprint( ec )
                    #pprint.pprint( self.importerProtein.proteinsInserted[ protein ] )
                    #pprint.pprint( protein )
                    pprint.pprint( self.importerEc.ecsInserted[ str(ec) ] )
                    #pprint.pprint( self.importerEc.ecsInserted )

        #pprint.pprint( self.importerProtein.proteinsInserted )
        #pprint.pprint( self.importerEc.ecsInserted)




