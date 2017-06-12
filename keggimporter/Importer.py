import pprint
from keggreader import *
from Config import *
from ImporterEc import *
from ImporterPathway import *
from ImporterOrganism import *
from AnendbFileSystem import *
from Logger import *
import sys
import subprocess
import collections

class Importer:
    """
    Load data from KeggReader and generates text insert files to be loaded, by Loader, into the PostgreSQL relational database.

    """

    def __init__( self ):

        self.primaryKeys = {}

        self.accessionsInserted     = {}
        self.taxonomiesInserted     = {}

        # This one is important to be ordered. There's 20 million proteins and when we're reading
        # data from an organism, we want to keep in memory the specific organisms data file (sometimes with thousands os lines) in memory and
        # switch to another organism only when the previous was completely read.
        self.proteinsInserted       = collections.OrderedDict()

        # Some importers does its job alone and it's called in this Importer.
        self.importerPathway  = ImporterPathway()
        self.importerEc       = ImporterEc()
        self.importerOrganism = ImporterOrganism()

        # Nothing really important, but it's being used to get the file name from a full path.
        # That's used to log what's happening in this class.
        # And log information here is extreme.
        # So, AnendbFileSystem can be removed if you remove the logging commands that calls it.
        self.afs              = AnendbFileSystem()

        # We have to log what's going to happen here.
        self.logger = None


    def startImporter( self ):

        self.reader = KeggReader()
        self.config = Config()
        self.afs    = AnendbFileSystem()

        self.config.loadConfiguration()
        self.conf = self.config.getConfigurations()

        # We have to log what's going to happen here.
        # And our logging system use the same configuration file as the Importer.
        configurationFile = self.config.getConfigurationFile()
        log = Logger()
        log.setConfigurationFile( configurationFile )
        self.logger = log.createLogSystem()


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

        # Our logging system use the same configuration file as the Importer.
        configurationFile = self.config.getConfigurationFile()
        log = Logger()
        log.setConfigurationFile( configurationFile )
        self.logger = log.createLogSystem()


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
        # Messing with this cute id will kill your importer because the table relationships files relies on that!!!
        # Take a look on the lines like 'taxonomiesInserted' or 'proteinsInserted'.
        return nextId


    def writePathways( self ): 
        """
        Only calls the class ImporterPathway methods to generate its insert instructions file.

        That's crucial because 'writePathways' generates a dictionary containing the primary key ids for pathways tables. 
        """

        self.logger.info( 'writePathways: START' )

        # Generate inserts for meabolic pathways.
        self.importerPathway.writePathways()

        self.logger.info( 'writePathways: DONE' )


    def writeEcs( self ): 
        """
        Only calls the class ImporterEc methods to generate its insert instructions file.

        That's crucial because 'writeEcs' generates a dictionary containing the primary key ids for pathways tables. 
        """

        self.logger.info( 'writeEcs: START' )

        # Generate inserts for ecs table.
        self.importerEc.writeEcs()

        self.logger.info( 'writeEcs: DONE' )


    def writeTaxonomies( self ):
        """
        Write the taxonomies insert file.

        """

        self.logger.info( 'writeTaxonomies: START' )

        self.logger.info( 'writeTaxonomies: keggreader.getAllOrganisms(): START' )

        organisms = self.reader.getAllOrganisms()

        self.logger.info( 'writeTaxonomies: keggreader.getAllOrganisms(): DONE' )

        taxonomies = {} 

        taxonomyFile = self.openInsertFile( 'taxonomiesInsert.psql' )

        self.logger.info( 'writeTaxonomies: We got ' + str(len(organisms)) + ' organisms and our insert file is taxonomiesInsert.psql' )


        for organism,taxonomyData in organisms.iteritems():
            for tax in taxonomyData['lineage']:

                taxonomies[ tax['name'] ] = { 'name': tax['name'], 'tax_id': tax['tax_id'], 'type': tax['type'] } 


        self.logger.info( 'writeTaxonomies: We got ' + str(len(taxonomies)) + ' taxonomies.' )


        for taxonomy,taxData in taxonomies.iteritems():
            taxonomyInserted = self.writeFile( taxonomyFile, 'taxonomies', [ str(taxData['name']), str(taxData['tax_id']), str(taxData['type']) ] )
            self.taxonomiesInserted[ taxData['name'] ] = taxonomyInserted

        self.logger.info( 'writeTaxonomies: DONE' )


    def writeOrganismTaxonomies( self ):
        """
        Write the insert file that relates organisms and its taxonomies.

        """

        self.logger.info( 'writeOrganismTaxonomies: START' )

        organisms = self.reader.getAllOrganisms()

        taxonomies = {} 

        self.logger.info( 'writeOrganismTaxonomies: insert file will be organismTaxonomiesInsert.psql' )

        taxonomyFile = self.openInsertFile( 'organismTaxonomiesInsert.psql' )

        for organism,taxonomyData in organisms.iteritems():
            for tax in taxonomyData['lineage']:

                taxId = self.taxonomiesInserted[ tax['name'] ] 
                organismId = self.importerOrganism.organismsInserted[ organism ] 

                self.writeFile( taxonomyFile, 'organism_taxonomies', [ str(organismId), str(taxId) ] )


        self.logger.info( 'writeOrganismTaxonomies: DONE' )
           

    def writeEcMaps( self ):
        """
        Write the insert file that relates EC numbers and metabolic map numbers.

        """

        self.logger.info( 'writeEcMaps: START' )

        self.logger.info( 'writeEcMaps: insert file will be ecMapsInsert.psql' )

        ecMapsFile = self.openInsertFile( 'ecMapsInsert.psql' )

        self.logger.info( 'writeEcMaps: keggreader.getEcMaps(): START' )

        ecMaps = self.reader.getEcMaps()

        self.logger.info( 'writeEcMaps: keggreader.getEcMaps(): START' )

        for ec,mapNumbers in ecMaps.iteritems():
            ecId = self.importerEc.ecsInserted[ ec ]
            
            for mapNumber in mapNumbers:

                if mapNumber in self.importerPathway.pathwayMapsInserted:

                    mapId = self.importerPathway.pathwayMapsInserted[ mapNumber ]

                    #self.writeEcMapsFile( ecMapsFile, ecId, mapId )
                    self.writeFile( ecMapsFile, 'ec_maps', [ str(ecId), str(mapId) ] )

        self.logger.info( 'writeEcMaps: DONE' )


    def writeProteinAccessions( self ):
        """
        Write insert file for the accessions protein ids.

        """

        self.logger.info( 'writeProteinAccessions: START' )

        self.logger.info( 'writeProteinAccessions: insert file will be proteinAccessionsInsert.psql' )

        proteinAccessionFile = self.openInsertFile( 'proteinAccessionsInsert.psql')

        for proteinIdentification, proteinIdRelationalDatabase in self.proteinsInserted.iteritems():
            accessionId = self.accessionsInserted[ proteinIdentification ]
            self.writeFile( proteinAccessionFile, 'protein_accessions', [ str(proteinIdRelationalDatabase), str(accessionId) ] )


        self.logger.info( 'writeProteinAccessions: DONE' )
 

    def writeOrganisms( self ): 
        """
        Write the insert file for the organisms table.

        """

        self.logger.info( 'writeOrganisms: START' )

        # Generate inserts for meabolic pathways.
        self.importerOrganism.writeOrganisms()
        

        self.logger.info( 'writeOrganisms: keggreader.getAllOrganismEcs() : START' )

        # Get all organism ecs relations.
        organismEcs = self.reader.getAllOrganismEcs()

        self.logger.info( 'writeOrganisms: keggreader.getAllOrganismEcs() : DONE' )


        self.logger.info( 'writeOrganisms: keggreader.getAllOrganismMaps() : START' )

        # Get all organism maps relations.
        organismMaps = self.reader.getAllOrganismMaps()

        self.logger.info( 'writeOrganisms: keggreader.getAllOrganismMaps() : DONE' )


        self.logger.info( 'writeOrganisms: organismEcFile is organismEcsInsert.psql' )

        # Open protein_ecs insert file.
        organismEcFile = self.openInsertFile( 'organismEcsInsert.psql' )


        self.logger.info( 'writeOrganisms: organismMapFile is organismMapsInsert.psql' )

        # Open organism_maps insert file.
        organismMapFile = self.openInsertFile( 'organismMapsInsert.psql' )


        # Now we have to write organism_ecs table.
        for organism,relationalDatabaseId in self.importerOrganism.organismsInserted.iteritems():


            organismId = relationalDatabaseId

            if len( organismEcs[ organism ] ) > 0:
                
                self.logger.info( 'writeOrganisms: the organism: ' + organism + ' : FOUND ' + str(len(organismEcs[organism])) + ' EC numbers.' )
                for ec in organismEcs[ organism ]:
                    ecId = self.importerEc.ecsInserted[ ec ]

                    #self.writeOrganismEcsFile( organismEcFile, organismId , ecId )
                    self.writeFile( organismEcFile, 'organism_ecs', [ str(organismId) , str(ecId) ] )
            else:
                self.logger.info( 'writeOrganisms: the organism: ' + organism + ' : doesnt have EC numbers associated.' )


            if len( organismMaps[ organism ] ) > 0:
                
                self.logger.info( 'writeOrganisms: the organism: ' + organism + ' : FOUND ' + str(len(organismMaps[organism])) + ' MAP numbers.' )
                for mapNumber in organismMaps[ organism ]:

                    # We don't need maps that is not metabolic maps.
                    if mapNumber in self.importerPathway.pathwayMapsInserted:
                        mapId = self.importerPathway.pathwayMapsInserted[ mapNumber ]

                        #self.writeOrganismMapsFile( organismMapFile, organismId , mapId )
                        self.writeFile( organismMapFile, 'organism_maps', [ str(organismId) , str(mapId) ] )
            else:
                self.logger.info( 'writeOrganisms: the organism: ' + organism + ' : doesnt have MAP numbers associated.' )


        self.logger.info( 'writeOrganisms: DONE' )


    def writeProteins( self ):
        """
        Write the proteins insert file.

        """

        self.logger.info( 'writeProteins: START' )

        proteinsDestination = self.openInsertFile( 'proteinsInsert.psql' )
        accessionsDestination = self.openInsertFile( 'accessionsInsert.psql' )

        proteins = {}

        totalOfSequences = self.reader.getTotalOfSequences()

        self.logger.info( 'writeProteins: total of sequences: ' + str(totalOfSequences) + '.' )

        files = self.reader.getPepFiles()

        self.logger.info( 'writeProteins: total of sequence files: ' + str(len(files)) + '.' )

        # For log purposes only!
        counter = 0

        for pepFile in files:
            f = self.reader.openPepFile( pepFile )

            positions = self.reader.getPepEntriesPositions()

            # Just for the log system.
            fileName = self.afs.getFileName( pepFile ) 
            self.logger.info( 'writeProteins: writing file: ' + str(fileName) + '.' )
            self.logger.info( 'writeProteins: file: ' + str(fileName) + ' have : ' + str(len(positions)) + ' entries.' )
            # END of log stuff.

            for position in positions:

                # Only log how long it's taking to run.
                # By thousands.
                counter += 1
                if ( counter % 100000 ) == 0:
                    self.logger.info( 'writeProtein: step: ' + str(counter) + '.')
                # END log step.


                entry = self.reader.getPepParsedEntry( position )

                # Sometimes there's 'pep' files without related organism. It happens in KEGG database.
                # We skip completely sequences without related organism.
                if not entry.organism.code in self.importerOrganism.organismsInserted:
                    self.logger.info( 'writeProteins: ORGANISM NOT FOUND: ' + entry.organism.code )

                    # Skip the 'pep' file completely.
                    break

                else:
                    organismId = self.importerOrganism.organismsInserted[ entry.organism.code ]

                    self.logger.info( 'writeProteins: writing entry : ' + str(entry.identification) + '.' )

                    #self.writeProteinsFile( proteinsDestination, entry.identification, entry.fullFastaHeader, entry.description, organismId, entry.sequence  )
                    proteinInserted = self.writeFile( proteinsDestination, 'proteins', [ str(entry.identification), str(entry.fullFastaHeader), str(entry.description), str(organismId), str(entry.sequence) ] )
                    self.proteinsInserted[ entry.identification ] = proteinInserted

                    accessionInserted = self.writeFile( accessionsDestination, 'accessions', [ str(entry.identification) ]  )
                    self.accessionsInserted[ entry.identification ] = accessionInserted 
                    #self.writeAccessionsFile( accessionsDestination, entry.identification  )


        self.logger.info( 'writeProteins: DONE' )


    def writeProteinRelations( self ): 
        """
        Write the insert file for some proteins relations like proteins and its EC numbers and proteins and its metabolic map numbers.

        """

        self.logger.info( 'writeProteinRelations: START' )

        self.logger.info( 'writeProteinRelations: keggreader.getAllProteinMaps() : START' )

        # Get all protein maps relations.
        # Notice that proteins without any map wont exist in the result below. That's important to save memory (no other reason at all).
        proteinMaps = self.reader.getAllProteinMaps()

        self.logger.info( 'writeProteinRelations: keggreader.getAllProteinMaps() : DONE' )


        self.logger.info( 'writeProteinRelations: proteinEcFile is: proteinEcsInsert.psql' )

        # Open protein_ecs insert file.
        proteinEcFile = self.openInsertFile( 'proteinEcsInsert.psql' )


        self.logger.info( 'writeProteinRelations: proteinMapFile is: proteinMapsInsert.psql' )

        # Open protein_maps insert file.
        proteinMapFile = self.openInsertFile( 'proteinMapsInsert.psql' )


        self.logger.info( 'writeProteinRelations: iterating through all the proteins: START' )

        # Keep a counter to know how long it's taking.
        counter = 0

        # Now we have to write protein_ecs table.
        # That means get the proteins ids and its related ecs ids.
        # Those ids comes from dictionary variables generated by the 'write' methods for each table.
        # So, we run through proteins ids and get ec from KeggReader 'getEcNumberByGene' method and make the correct relation.
        for protein,relationalDatabaseId in self.proteinsInserted.iteritems():

            # Only log how long it's taking to run.
            # By thousands.
            counter += 1
            if ( counter % 100000 ) == 0:
                self.logger.info( 'writeProteinRelations: step: ' + str(counter) + '.')
            # END log step.

            self.logger.info( 'writeProteinRelations: keggreader.getEcNumbersByGene(): START' )

            # We get all EC numbers related to the specific protein.
            ecs = self.reader.getEcNumberByGene( protein ) 

            self.logger.info( 'writeProteinRelations: keggreader.getEcNumbersByGene(): DONE' )

            # If there's EC number (almost of proteins doesn't has a related EC number - which means they're no enzymes).
            if ecs:

                self.logger.info( 'writeProteinRelations: FOUND EC Numbers for the protein: ' + str(protein) + '.' )
                self.logger.info( 'writeProteinRelations: ' + str(protein) + ' : Total of EC Numbers FOUND: ' + str(len(ecs)) + '.' )

                # Iterate through the ECs found for that specific protein.
                for ec in ecs:
                    # Get the relational database EC id for that EC number being iterated 
                    ecId = self.importerEc.ecsInserted[ str(ec) ] 
                    proteinId = relationalDatabaseId

                    # Actual write protein_ecs file.
                    #self.writeProteinEcsFile( proteinEcFile, proteinId, ecId )
                    self.writeFile( proteinEcFile, 'protein_ecs', [ str(proteinId), str(ecId) ] )
            else:
                self.logger.info( 'writeProteinRelations: NOT FOUND EC Numbers for the protein: ' + str(protein) + '.' )


            # Maps to specific protein.
            if protein in proteinMaps:
                maps = proteinMaps[ protein ]

                if maps:
                    self.logger.info( 'writeProteinRelations: FOUND MAP Numbers for the protein: ' + str(protein) + '.' )
                    self.logger.info( 'writeProteinRelations: ' + str(protein) + ' : Total of MAP Numbers FOUND: ' + str(len(maps)) + '.' )

                    for proteinMap in maps:

                        # Some maps aren't metabolic pathways but simple pathways for other molecular mechanisms.
                        # And we're interested only in metabolic maps at this moment.
                        if proteinMap in self.importerPathway.pathwayMapsInserted:
                            mapId     = self.importerPathway.pathwayMapsInserted[ proteinMap ]
                            proteinId = relationalDatabaseId

                            #self.writeProteinMapsFile( proteinMapFile, proteinId, mapId )
                            self.writeFile( proteinMapFile, 'protein_maps', [ str(proteinId), str(mapId) ] )
            else:
                self.logger.info( 'writeProteinRelations: NOT FOUND MAP Numbers for the protein: ' + str(protein) + '.' )


        self.logger.info( 'writeProteinRelations: iterating through all the proteins: DONE' )
        self.logger.info( 'writeProteinRelations: DONE' )


