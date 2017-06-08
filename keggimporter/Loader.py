import pprint
from keggreader import *
from Config import *
from ImporterEc import *
from ImporterPathway import *
from ImporterOrganism import *
import sys
import subprocess
from time import sleep

class Importer:

    def __init__( self ):

        self.files = None

    def start( self ):

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


    def loadFiles( self ):

        dataSource = self.getConfiguration( 'directories', 'inserts' )
        username   = self.getConfiguration( 'database', 'user' )

        self.files = [
                    { 'file': 'ecsInsert.psql',                 'table': 'ecs', 'columns': [ 'id', 'ec' ] },
                    { 'file': 'organismsInsert.psql',           'table': 'organisms', 'columns': [ 'id', 'code', 'name', 'internal_id', 'taxonomy_id' ] },
                    { 'file': 'pathwaySuperClassesInsert.psql', 'table': 'pathway_super_classes', 'columns': [ 'id', 'name' ] },
                    { 'file': 'pathwayClassesInsert.psql',      'table': 'pathway_classes', 'columns': [ 'id', 'super_class_id', 'name' ] },
                    { 'file': 'pathwayNamesInsert.psql',        'table': 'pathway_maps', 'columns': [ 'id', 'class_id', 'identification', 'name' ] } ,
                    { 'file': 'taxonomiesInsert.psql',          'table': 'taxonomies', 'columns': [ 'id', 'taxonomy', 'tax_id', 'tax_type' ] },
                    { 'file': 'organismTaxonomiesInsert.psql',  'table': 'organism_taxonomies', 'columns': [ 'id', 'organism_id', 'taxonomy_id' ] },
                    { 'file': 'proteinsInsert.psql',            'table': 'proteins', 'columns': [ 'id', 'identification', 'full_fasta_header', 'description', 'organism_id', 'sequence' ] },
                    { 'file': 'proteinEcsInsert.psql',          'table': 'protein_ecs', 'columns': [ 'id', 'protein_id', 'ec_id' ] },
                    { 'file': 'proteinMapsInsert.psql',         'table': 'protein_maps', 'columns': [ 'id', 'protein_id', 'map_id' ] },
                    { 'file': 'organismEcsInsert.psql',         'table': 'organism_ecs', 'columns': [ 'id', 'organism_id', 'ec_id' ] },
                    { 'file': 'organismMapsInsert.psql',        'table': 'organism_maps', 'columns': [ 'id', 'organism_id', 'map_id' ] },
                    { 'file': 'accessionsInsert.psql',          'table': 'accessions', 'columns': [ 'id', 'accession' ] },
                    { 'file': 'proteinAccessionsInsert.psql',   'table': 'protein_accessions', 'columns': [ 'id', 'protein_id', 'accession_id' ] },
                    { 'file': 'ecMapsInsert.psql',              'table': 'ec_maps', 'columns': [ 'id', 'ec_id', 'map_id' ] },
                 ]

        # Load each table into relational database.
        for loadFile in self.files:

            pprint.pprint( '-----------------------------------------------' )
            pprint.pprint( loadFile['file'] )
            pprint.pprint( '-----------------------------------------------' )
            print( "\n" )
            fileToLoad = dataSource + '/' + loadFile['file'] 
            table = loadFile['table']
            columns = ','.join( loadFile['columns'] )

            subprocess.Popen( "psql -U " + username + " -c \"\copy " + table + "(" + columns + ") from \'" + fileToLoad + "\';\"", shell=True )
            sleep( 2 )




