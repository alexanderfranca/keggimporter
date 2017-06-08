import pprint
from keggreader import *
from Config import *
import sys


# TODO: Remove code duplication. All the 'open', 'next' and 'write file' methods can be replaced by a single one.
#       Take a look in the Importer.py class to see how it can be done.
class ImporterPathway:

    def __init__( self ):

        self.pathwaySuperClassPrimaryKey = 0
        self.pathwaySuperClassesInserted  = {}

        self.pathwayClassPrimaryKey = 0
        self.pathwayClassesInserted  = {}

        self.pathwayNamePrimaryKey = 0
        self.pathwayNamesInserted  = {}
        self.pathwayMapsInserted   = {}


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


    def openPathwaySuperClassesFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'pathwaySuperClassesInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def openPathwayClassesFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'pathwayClassesInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def openPathwayNamesFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'pathwayNamesInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def nextPathwaySuperClassPrimaryKey( self ):
        """
        Controls the pathways table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.pathwaySuperClassPrimaryKey += 1

        return self.pathwaySuperClassPrimaryKey


    def nextPathwayClassPrimaryKey( self ):
        """
        Controls the pathways table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.pathwayClassPrimaryKey += 1

        return self.pathwayClassPrimaryKey


    def nextPathwayNamePrimaryKey( self ):
        """
        Controls the pathways table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.pathwayNamePrimaryKey += 1

        return self.pathwayNamePrimaryKey


    def writePathwaySuperClassesFile( self, pathway_super_classes_file=None, pathway_super_class=None ):
        """
        Actual write the pathways inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextPathwaySuperClassPrimaryKey()

        pathway_super_classes_file.write( str(nextId) + '\t' + str(pathway_super_class) + "\n" )

        self.pathwaySuperClassesInserted[ str( pathway_super_class ) ] = nextId 


    def writePathwayClassesFile( self, pathway_classes_file=None, pathway_super_class_id=None, pathway_class=None ):
        """
        Actual write the pathways inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextPathwayClassPrimaryKey()

        pathway_classes_file.write( str(nextId) + '\t' + str( pathway_super_class_id ) + '\t' + str(pathway_class) + "\n" )

        self.pathwayClassesInserted[ str( pathway_class ) ] = nextId 


    def writePathwayNamesFile( self, pathway_names_file=None, pathway_class_id=None, pathway_map=None, pathway_name=None ):
        """
        Actual write the pathways inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextPathwayNamePrimaryKey()

        pathway_names_file.write( str(nextId) + '\t' + str( pathway_class_id ) + '\t' + str(pathway_map) + '\t' + str(pathway_name) + "\n" )

        self.pathwayNamesInserted[ str( pathway_name ) ] = nextId 
        self.pathwayMapsInserted[ str( pathway_map ) ] = nextId


    def writePathways( self ):
        """
        Write the pathways insert file.
        """

        pathwaysDestination      = self.openPathwaySuperClassesFile()
        pathwaysClassDestination = self.openPathwayClassesFile()
        pathwaysNamesDestination = self.openPathwayNamesFile()

        pathways = self.reader.getAllPathways() 
        
        # Pathway super class
        for pathwaySuperClass, pathwayData in pathways.iteritems():
            self.writePathwaySuperClassesFile( pathwaysDestination, pathwaySuperClass )

            # Pathway class
            for pathwayClass,data in pathwayData.iteritems():
                self.writePathwayClassesFile( pathwaysClassDestination, self.pathwaySuperClassesInserted[ pathwaySuperClass ], pathwayClass )

                # Pathway map and name
                for pathwayMap,pathwayName in data.iteritems():
                    self.writePathwayNamesFile( pathwaysNamesDestination, self.pathwayClassesInserted[ pathwayClass ], pathwayMap, pathwayName )







