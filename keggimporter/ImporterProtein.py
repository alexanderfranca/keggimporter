import pprint
from keggreader import *
from Config import *
import sys
import cPickle

class ImporterProtein:

    def __init__( self ):

        self.proteinPrimaryKey = 0
        self.proteinsInserted  = {}

        self.accessionPrimaryKey = 0
        self.accessionsInserted  = {}


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


    def openProteinsFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'proteinsInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def openAccessionsFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'accessionsInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def nextProteinPrimaryKey( self ):
        """
        Controls the proteins table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.proteinPrimaryKey += 1

        return self.proteinPrimaryKey


    def nextAccessionPrimaryKey( self ):
        """
        Controls the proteins table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.accessionPrimaryKey += 1

        return self.accessionPrimaryKey



    def writeProteinsFile( self, protein_file=None, identification=None, full_fasta_header=None, description=None, sequence=None ):
        """
        Actual write the proteins inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextProteinPrimaryKey()

        protein_file.write( str(nextId) + '\t' + str(identification) + '\t' + str(full_fasta_header) + '\t' + str(description) + '\t' + str(sequence) + "\n" )

        self.proteinsInserted[ str(identification ) ] = nextId 
        

    def writeAccessionsFile( self, accession_file=None, accession=None ):
        """
        Actual write the proteins inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextAccessionPrimaryKey()

        accession_file.write( str(nextId) + '\t' + str(accession) + "\n" )

        self.accessionsInserted[ str(accession) ] = nextId 
        


    def writeProteins( self ):
        """
        Write the proteins insert file.
        """

        proteinsDestination = self.openProteinsFile()
        accessionsDestination = self.openAccessionsFile()

        proteins = {}

        files = self.reader.getPepFiles()

        for pepFile in files:
            f = self.reader.openPepFile( pepFile )

            positions = self.reader.getPepEntriesPositions()

            for position in positions:

                entry = self.reader.getPepParsedEntry( position )

                #pprint.pprint( entry.organism.code )

                self.writeProteinsFile( proteinsDestination, entry.identification, entry.fullFastaHeader, entry.description, entry.sequence  )
                self.writeAccessionsFile( accessionsDestination, entry.identification  )








