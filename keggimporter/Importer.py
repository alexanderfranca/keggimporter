import pprint
from keggreader import *
from Config import *
from ImporterEc import *
from ImporterPathway import *
from ImporterOrganism import *
import sys
import subprocess
import collections

class Importer:

    def __init__( self ):

        self.primaryKeys = {}

        self.accessionsInserted     = {}
        self.proteinsInserted       = collections.OrderedDict()
        self.taxonomiesInserted     = {}

        self.importerPathway  = ImporterPathway()
        self.importerEc       = ImporterEc()
        self.importerOrganism = ImporterOrganism()
        #self.reader           = KeggReader()


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


    def openInsertFile( self, file_name=None ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = file_name 

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def nextPrimaryKey( self, table_key=None ):
        """
        Returns the next primary key id for an specific table.

        Args:
            table_key(str): Name of the table.

        Returns:
            (int): The next primary key id.

        """

        # Make sure the dictionary key exists and, if not, create with zero as starting value.
        if not table_key in self.primaryKeys:
            self.primaryKeys[ table_key ] = 0


        # Increment the id.
        self.primaryKeys[ table_key ] += 1

        return self.primaryKeys[ table_key ]


    def writeFile( self, file_handle=None, table_name=None, data=None ):
        """
        Write the actual insert instructions file.

        Args:
            file_handle(file): File handle where to write the data.
            table_name(str): Name of the table. This one is subjective, it means 'table_name' is the key name used by a class dictionary variable to keep tracking of the primary key ids.
            data(list): List of string to be written in the file.

        """

        # Record the next primary key id.
        nextId = self.nextPrimaryKey( table_name )

        # Generate the string list of data to be written in the file.
        values = '\t'.join( data )

        # Actual put together the primary key id, the string values and the new line character to be writen in the file.
        insert = str(nextId) + '\t' + str(values) + "\n"

        # Write the stuff in the file.
        file_handle.write( insert )

        # DON'T MESS WITH THAT!!!!! YOU'RE WARNED!!!
        # Messing with this cute id will kill your importer because the table relationships generation files relies on that!!!
        # Take a look on the lines like 'taxonomiesInserted' or 'proteinsInserted'.
        return nextId


    def writePathways( self ): 
        """
        Only calls the class ImporterPathway methods to generate its insert instructions file.

        That's crucial because 'writePathways' generates a dictionary containing the primary key ids for pathways tables. 
        """

        # Generate inserts for meabolic pathways.
        self.importerPathway.writePathways()


    def writeEcs( self ): 
        """
        Only calls the class ImporterEc methods to generate its insert instructions file.

        That's crucial because 'writeEcs' generates a dictionary containing the primary key ids for pathways tables. 
        """

        # Generate inserts for ecs table.
        self.importerEc.writeEcs()


    def writeTaxonomies( self ):
        """
        Write the taxonomies insert file.

        """
        organisms = self.reader.getAllOrganisms()

        taxonomies = {} 

        taxonomyFile = self.openInsertFile( 'taxonomiesInsert.psql' )

        for organism,taxonomyData in organisms.iteritems():
            for tax in taxonomyData['lineage']:

                taxonomies[ tax['name'] ] = { 'name': tax['name'], 'tax_id': tax['tax_id'], 'type': tax['type'] } 


        for taxonomy,taxData in taxonomies.iteritems():
            taxonomyInserted = self.writeFile( taxonomyFile, 'taxonomies', [ str(taxData['name']), str(taxData['tax_id']), str(taxData['type']) ] )
            self.taxonomiesInserted[ taxData['name'] ] = taxonomyInserted



    def writeOrganismTaxonomies( self ):
        """
        Write the insert file that relates organisms and its taxonomies.
        """

        organisms = self.reader.getAllOrganisms()

        taxonomies = {} 

        taxonomyFile = self.openInsertFile( 'organismTaxonomiesInsert.psql' )

        for organism,taxonomyData in organisms.iteritems():
            for tax in taxonomyData['lineage']:

                taxId = self.taxonomiesInserted[ tax['name'] ] 
                organismId = self.importerOrganism.organismsInserted[ organism ] 

                self.writeFile( taxonomyFile, 'organism_taxonomies', [ str(organismId), str(taxId) ] )
           

    def writeEcMaps( self ):
        """
        Write the insert file that relates EC numbers and metabolic map numbers.

        """

        ecMapsFile = self.openInsertFile( 'ecMapsInsert.psql' )

        ecMaps = self.reader.getEcMaps()

        for ec,mapNumbers in ecMaps.iteritems():
            ecId = self.importerEc.ecsInserted[ ec ]
            
            for mapNumber in mapNumbers:

                if mapNumber in self.importerPathway.pathwayMapsInserted:

                    mapId = self.importerPathway.pathwayMapsInserted[ mapNumber ]

                    #self.writeEcMapsFile( ecMapsFile, ecId, mapId )
                    self.writeFile( ecMapsFile, 'ec_maps', [ str(ecId), str(mapId) ] )


    def writeProteinAccessions( self ):
        """
        Write insert file for the accessions protein ids.

        """

        proteinAccessionFile = self.openInsertFile( 'proteinAccessionsInsert.psql')

        for proteinIdentification, proteinIdRelationalDatabase in self.proteinsInserted.iteritems():
            accessionId = self.accessionsInserted[ proteinIdentification ]
            self.writeFile( proteinAccessionFile, 'protein_accessions', [ str(proteinIdRelationalDatabase), str(accessionId) ] )

 

    def writeOrganisms( self ): 
        """
        Write the insert file for the organisms table.

        """

        # Generate inserts for meabolic pathways.
        self.importerOrganism.writeOrganisms()
        
        # Get all organism ecs relations.
        organismEcs = self.reader.getAllOrganismEcs()

        # Get all organism maps relations.
        organismMaps = self.reader.getAllOrganismMaps()

        # Open protein_ecs insert file.
        organismEcFile = self.openInsertFile( 'organismEcsInsert.psql' )

        # Open organism_maps insert file.
        organismMapFile = self.openInsertFile( 'organismMapsInsert.psql' )


        # Now we have to write organism_ecs table.
        # That means get the proteins ids and its related ecs ids.
        # Those ids comes from dictionary variables generated by the 'write' methods for each table.
        # So, we run through proteins ids and get ec from KeggReader 'getEcNumberByGene' method and make the correct relation.
        for organism,relationalDatabaseId in self.importerOrganism.organismsInserted.iteritems():


            organismId = relationalDatabaseId

            if len( organismEcs[ organism ] ) > 0:
                
                for ec in organismEcs[ organism ]:
                    ecId = self.importerEc.ecsInserted[ ec ]

                    #self.writeOrganismEcsFile( organismEcFile, organismId , ecId )
                    self.writeFile( organismEcFile, 'organism_ecs', [ str(organismId) , str(ecId) ] )

            if len( organismMaps[ organism ] ) > 0:
                
                for mapNumber in organismMaps[ organism ]:

                    # We don't need maps that is not metabolic maps.
                    if mapNumber in self.importerPathway.pathwayMapsInserted:
                        mapId = self.importerPathway.pathwayMapsInserted[ mapNumber ]

                        #self.writeOrganismMapsFile( organismMapFile, organismId , mapId )
                        self.writeFile( organismMapFile, 'organism_maps', [ str(organismId) , str(mapId) ] )


    def writeProteins( self ):
        """
        Write the proteins insert file.

        """

        proteinsDestination = self.openInsertFile( 'proteinsInsert.psql' )
        accessionsDestination = self.openInsertFile( 'accessionsInsert.psql' )

        proteins = {}

        files = self.reader.getPepFiles()

        for pepFile in files:
            f = self.reader.openPepFile( pepFile )

            positions = self.reader.getPepEntriesPositions()

            for position in positions:

                entry = self.reader.getPepParsedEntry( position )

                organismId = self.importerOrganism.organismsInserted[ entry.organism.code ]

                #self.writeProteinsFile( proteinsDestination, entry.identification, entry.fullFastaHeader, entry.description, organismId, entry.sequence  )
                proteinInserted = self.writeFile( proteinsDestination, 'proteins', [ str(entry.identification), str(entry.fullFastaHeader), str(entry.description), str(organismId), str(entry.sequence) ] )
                self.proteinsInserted[ entry.identification ] = proteinInserted

                accessionInserted = self.writeFile( accessionsDestination, 'accessions', [ str(entry.identification) ]  )
                self.accessionsInserted[ entry.identification ] = accessionInserted 
                #self.writeAccessionsFile( accessionsDestination, entry.identification  )



    def writeProteinRelations( self ): 
        """
        Write the insert file for some proteins relations like proteins and its EC numbers and proteins and its metabolic map numbers.

        """

        # Get all protein maps relations.
        # Notice that proteins without any map wont exist in the result below. That's important to save memory (no other reason at all).
        proteinMaps = self.reader.getAllProteinMaps()

        # Open protein_ecs insert file.
        proteinEcFile = self.openInsertFile( 'proteinEcsInsert.psql' )

        # Open protein_maps insert file.
        proteinMapFile = self.openInsertFile( 'proteinMapsInsert.psql' )

        # Now we have to write protein_ecs table.
        # That means get the proteins ids and its related ecs ids.
        # Those ids comes from dictionary variables generated by the 'write' methods for each table.
        # So, we run through proteins ids and get ec from KeggReader 'getEcNumberByGene' method and make the correct relation.
        for protein,relationalDatabaseId in self.proteinsInserted.iteritems():

            # We get all EC numbers related to the specific protein.
            ecs = self.reader.getEcNumberByGene( protein ) 

            # If there's EC number (almost of proteins doesn't has a related EC number - which means they're no enzymes).
            if ecs:

                # Iterate through the ECs found for that specific protein.
                for ec in ecs:
                    # Get the relational database EC id for that EC number being iterated 
                    ecId = self.importerEc.ecsInserted[ str(ec) ] 
                    proteinId = relationalDatabaseId

                    # Actual write protein_ecs file.
                    #self.writeProteinEcsFile( proteinEcFile, proteinId, ecId )
                    self.writeFile( proteinEcFile, 'protein_ecs', [ str(proteinId), str(ecId) ] )


            # Maps to specific protein.
            if protein in proteinMaps:
                maps = proteinMaps[ protein ]

                if maps:
                    for proteinMap in maps:

                        # Some maps aren't metabolic pathways but simple pathways for other molecular mechanisms.
                        # And we're interested only in metabolic maps at this moment.
                        if proteinMap in self.importerPathway.pathwayMapsInserted:
                            mapId     = self.importerPathway.pathwayMapsInserted[ proteinMap ]
                            proteinId = relationalDatabaseId

                            #self.writeProteinMapsFile( proteinMapFile, proteinId, mapId )
                            self.writeFile( proteinMapFile, 'protein_maps', [ str(proteinId), str(mapId) ] )




