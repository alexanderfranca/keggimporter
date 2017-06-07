import pprint
from keggreader import *
from Config import *
from ImporterProtein import *
from ImporterEc import *
from ImporterPathway import *
from ImporterOrganism import *
import sys

class Importer:

    def __init__( self ):

        self.proteinEcsPrimaryKey         = 0 
        self.proteinMapsPrimaryKey        = 0
        self.organismEcsPrimaryKey        = 0
        self.organismMapsPrimaryKey       = 0
        self.taxonomyPrimaryKey           = 0
        self.proteinPrimaryKey            = 0
        self.accessionPrimaryKey          = 0
        self.organismTaxonomiesPrimaryKey = 0

        self.accessionsInserted     = {}
        self.proteinsInserted       = {}
        self.taxonomiesInserted     = {}

        self.importerPathway  = ImporterPathway()
        self.importerEc       = ImporterEc()
        self.importerOrganism = ImporterOrganism()
        self.reader           = KeggReader()


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


    def openProteinMapsFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'proteinMapsInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def openOrganismEcsFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'organismEcsInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


    def openOrganismMapsFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'organismMapsInsert.psql'

        filePath = destinationDirectory + '/' + fileName

        if self.afs.fileExists( filePath ):
            fileHandle = self.afs.purgeAndCreateFile( filePath )
        else:
            fileHandle = self.afs.openFileForAppend( filePath )

        return fileHandle


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


    def openOrganismTaxonomiesFile( self ):
        """
        Opens the file where to store database inserts instructions.

        Returns:
            (file): File handle to be written.

        """

        destinationDirectory = self.getConfiguration( 'directories', 'inserts' ) 

        fileName = 'organismTaxonomiesInsert.psql'

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


    def nextTaxonomyPrimaryKey( self ):
        """
        Controls the proteins table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.taxonomyPrimaryKey += 1

        return self.taxonomyPrimaryKey


    def nextAccessionPrimaryKey( self ):
        """
        Controls the proteins table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.accessionPrimaryKey += 1

        return self.accessionPrimaryKey


    def nextProteinEcsPrimaryKey( self ):
        """
        Controls the proteins table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.proteinEcsPrimaryKey += 1

        return self.proteinEcsPrimaryKey


    def nextProteinMapsPrimaryKey( self ):
        """
        Controls the proteins table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.proteinMapsPrimaryKey += 1

        return self.proteinMapsPrimaryKey


    def nextOrganismEcsPrimaryKey( self ):
        """
        Controls the proteins table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.organismEcsPrimaryKey += 1

        return self.organismEcsPrimaryKey


    def nextOrganismMapsPrimaryKey( self ):
        """
        Controls the proteins table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.organismMapsPrimaryKey += 1

        return self.organismMapsPrimaryKey


    def nextOrganismTaxonomiesPrimaryKey( self ):
        """
        Controls the proteins table primary key counter.

        Returns:
            (int): An integer representing the new primary key.

        """

        self.organismTaxonomiesPrimaryKey += 1

        return self.organismTaxonomiesPrimaryKey



    def writeProteinsFile( self, protein_file=None, identification=None, full_fasta_header=None, description=None, organism_id=None, sequence=None ):
        """
        Actual write the proteins inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextProteinPrimaryKey()

        protein_file.write( str(nextId) + '\t' + str(identification) + '\t' + str(full_fasta_header) + '\t' + str(description) + '\t' + str(organism_id) + '\t' + str(sequence) + "\n" )

        self.proteinsInserted[ str(identification ) ] = nextId 
        

    def writeAccessionsFile( self, accession_file=None, accession=None ):
        """
        Actual write the proteins inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextAccessionPrimaryKey()

        accession_file.write( str(nextId) + '\t' + str(accession) + "\n" )

        self.accessionsInserted[ str(accession) ] = nextId 
 


    def writeProteinEcsFile( self, protein_ecs_file=None, protein_id=None, ec_id=None ):
        """
        Actual write the protein_ecs inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextProteinEcsPrimaryKey()

        protein_ecs_file.write( str(nextId) + '\t' + str(protein_id) + '\t' + str(ec_id) + "\n" )

        #self.proteinEcsInserted[ str(identification ) ] = nextId 
        

    def writeProteinMapsFile( self, protein_maps_file=None, protein_id=None, map_id=None ):
        """
        Actual write the protein_maps inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextProteinMapsPrimaryKey()

        protein_maps_file.write( str(nextId) + '\t' + str(protein_id) + '\t' + str(map_id) + "\n" )

        #self.proteinEcsInserted[ str(identification ) ] = nextId 


    def writeOrganismEcsFile( self, organism_ecs_file=None, organism_id=None, ec_id=None ):
        """
        Actual write the organism_ecs inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextOrganismEcsPrimaryKey()

        organism_ecs_file.write( str(nextId) + '\t' + str(organism_id) + '\t' + str(ec_id) + "\n" )

        #self.proteinEcsInserted[ str(identification ) ] = nextId 


    def writeOrganismMapsFile( self, organism_maps_file=None, organism_id=None, map_id=None ):
        """
        Actual write the organism_ecs inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextOrganismMapsPrimaryKey()

        organism_maps_file.write( str(nextId) + '\t' + str(organism_id) + '\t' + str(map_id) + "\n" )

        #self.proteinEcsInserted[ str(identification ) ] = nextId 
 

    def writeTaxonomiesFile( self, taxonomy_file=None, taxonomy=None, tax_id=None, tax_type=None ):
        """
        Actual write the taxonomies inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextTaxonomyPrimaryKey()

        taxonomy_file.write( str(nextId) + '\t' + str(taxonomy) + '\t' + str(tax_id) + '\t' + str(tax_type) + "\n" )

        self.taxonomiesInserted[ str(taxonomy) ] = nextId 


    def writeOrganismTaxonomiesFile( self, organism_taxonomies_file=None, organism_id=None, taxonomy_id=None ):
        """
        Actual write the organism_taxonomies inserts file, log the operation and keep the inserted ids.
        """

        nextId = self.nextOrganismTaxonomiesPrimaryKey()
        
        organism_taxonomies_file.write( str(nextId) + '\t' + str(organism_id) + '\t' + str(taxonomy_id) + "\n" )



    # TODO: test, comments
    def writePathways( self ): 

        # Generate inserts for meabolic pathways.
        self.importerPathway.writePathways()


    # TODO: test, comments
    def writeEcs( self ): 

        # Generate inserts for ecs table.
        self.importerEc.writeEcs()


    def writeTaxonomies( self ):

        organisms = self.reader.getAllOrganisms()

        taxonomies = {} 

        taxonomyFile = self.openTaxonomiesFile()

        for organism,taxonomyData in organisms.iteritems():
            for tax in taxonomyData['lineage']:

                taxonomies[ tax['name'] ] = { 'name': tax['name'], 'tax_id': tax['tax_id'], 'type': tax['type'] } 


        for taxonomy,taxData in taxonomies.iteritems():
            self.writeTaxonomiesFile( taxonomyFile, taxData['name'], taxData['tax_id'], taxData['type'] )


    def writeOrganismTaxonomies( self ):

        organisms = self.reader.getAllOrganisms()

        taxonomies = {} 

        taxonomyFile = self.openOrganismTaxonomiesFile()

        for organism,taxonomyData in organisms.iteritems():
            for tax in taxonomyData['lineage']:

                taxId = self.taxonomiesInserted[ tax['name'] ] 
                organismId = self.importerOrganism.organismsInserted[ organism ] 

                self.writeOrganismTaxonomiesFile( taxonomyFile, taxId, organismId )
           

 
    # TODO: test, comments
    def writeOrganisms( self ): 

        # Generate inserts for meabolic pathways.
        self.importerOrganism.writeOrganisms()
        
        # Get all organism ecs relations.
        organismEcs = self.reader.getAllOrganismEcs()

        # Get all organism maps relations.
        organismMaps = self.reader.getAllOrganismMaps()

        # Open protein_ecs insert file.
        organismEcFile = self.openOrganismEcsFile()

        # Open organism_maps insert file.
        organismMapFile = self.openOrganismMapsFile()


        # Now we have to write organism_ecs table.
        # That means get the proteins ids and its related ecs ids.
        # Those ids comes from dictionary variables generated by the 'write' methods for each table.
        # So, we run through proteins ids and get ec from KeggReader 'getEcNumberByGene' method and make the correct relation.
        for organism,relationalDatabaseId in self.importerOrganism.organismsInserted.iteritems():


            organismId = relationalDatabaseId

            if len( organismEcs[ organism ] ) > 0:
                
                for ec in organismEcs[ organism ]:
                    ecId = self.importerEc.ecsInserted[ ec ]

                    self.writeOrganismEcsFile( organismEcFile, organismId , ecId )

            if len( organismMaps[ organism ] ) > 0:
                
                for mapNumber in organismMaps[ organism ]:

                    # We don't need maps that is not metabolic maps.
                    if mapNumber in self.importerPathway.pathwayMapsInserted:
                        mapId = self.importerPathway.pathwayMapsInserted[ mapNumber ]

                        self.writeOrganismMapsFile( organismMapFile, organismId , mapId )


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

                organismId = self.importerOrganism.organismsInserted[ entry.organism.code ]

                self.writeProteinsFile( proteinsDestination, entry.identification, entry.fullFastaHeader, entry.description, organismId, entry.sequence  )
                self.writeAccessionsFile( accessionsDestination, entry.identification  )





    # TODO: test, comments
    def writeProteinRelations( self ): 

#        # Generate inserts for meabolic pathways.
#        self.importerPathway.writePathways()
#        
#        # Generate inserts for proteins table.
#        self.importerProtein.writeProteins()
#
#        # Generate inserts for ecs table.
#        self.importerEc.writeEcs()
#
        # Get all protein maps relations.
        # Notice that proteins without any map wont exist in the result below. That's important to save memory (no other reason at all).
        proteinMaps = self.reader.getAllProteinMaps()

        # Open protein_ecs insert file.
        proteinEcFile = self.openProteinEcsFile()

        # Open protein_maps insert file.
        proteinMapFile = self.openProteinMapsFile()


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
                    self.writeProteinEcsFile( proteinEcFile, proteinId, ecId )


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

                            self.writeProteinMapsFile( proteinMapFile, proteinId, mapId )




