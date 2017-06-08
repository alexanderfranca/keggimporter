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


    def loadFiles( self ):


        filesToRun = [

         { 'file': 'ecsInsert.psql',                 'columns': [ 'id', 'ec' ] },
         { 'file': 'organismsInsert.psql',           'columns': [ 'id', 'organism_code', 'organism_kegg_name', 'organism_internal_kegg_id', 'taxonomy_id' ] },
         { 'file': 'pathwaySuperClassesInsert.psql', 'columns': [ 'id', 'name' ] },
         { 'file': 'pathwayClassesInsert.psql',      'columns': [ 'id', 'super_class_id', 'name' ] },
         { 'file': 'pathwayNamesInsert.psql',        'columns': [ 'id', 'class_id', 'map_number', 'name' ] } ,
         { 'file': 'taxonomiesInsert.psql',          'columns': [ 'id', 'taxonomy', 'tax_id', 'tax_type' ] },
         { 'file': 'organismTaxonomiesInsert.psql',  'columns': [ 'id', 'organism_id', 'taxonomy_id' ] },
         { 'file': 'proteinsInsert.psql',            'columns': [ 'id', 'identification', 'full_fasta_header', 'description', 'organism_id', 'sequence' ] },
         { 'file': 'proteinEcsInsert.psql',          'columns': [ 'id', 'protein_id', 'ec_id' ] },
         { 'file': 'proteinMapsInsert.psql',         'columns': [ 'id', 'protein_id', 'map_id' ] },,
         { 'file': 'organismEcsInsert.psql',         'columns': [ 'id', 'organism_id', 'ec_id' ] },
         { 'file': 'organismMapsInsert.psql',        'columns': [ 'id', 'organism_id', 'map_id' ] },
         { 'file': 'accessionsInsert.psql',          'columns': [ 'id', 'accession' ] },
         { 'file': 'proteinAccessionsInsert.psql',   'columns': [ 'id', 'protein_id', 'accession_id' ] },

    ]
#subprocess.Popen('psql ' + args.database_name + ' -U ' + args.database_name + " -c 'create index on genome_comparison_clusters(protein_ids);'", shell=True)
#subprocess.Popen('psql ' + args.database_name + ' -U ' + args.database_name + " -c 'create index on genome_comparison_clusters(genome_comparison_id);'", shell=True)





