import pprint
from keggreader import *
from Config import *
from ImporterEc import *
from ImporterPathway import *
from ImporterOrganism import *
import sys
import subprocess
import re
import glob

class Loader:
    """
    This class loads the insert instructions data files into the relational database.

    Relational databases can be very messy and crazy.

    This class doesn't relies in the database administrators.

    But at the same time it isn't the best example of generalization.

    That's because this class is supposed to be manipulated at every time you need to load a new relational database.

    And as you can see in the code, everything is so clear in you face.

    Read the code, make the changes (keep a backup) and run it.

    """

    def __init__( self ):

        # THIS --> IS <-- THE EXPECTED RELATIONAL DATABASE TABLES AND COLUMNS!!!
        # AND!!!! THE COLUMN ORDER MATTERS!!
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


    def start( self ):
        """
        Actual it only loads the destination directory to put the instructions insert files.

        """

        self.config = Config()
        self.afs    = AnendbFileSystem()

        self.config.loadConfiguration()
        self.conf = self.config.getConfigurations()


    def checkPsqlCanExecuteCommand( self ):
        """
        Check if this loader can execute 'psql' commands.

        If not... nothing is going to work.

        Returns:
            (boolean): True (you can do stuff in PostgreSQL), False (you're screwed, call for help, it's a loader, don't expect to be happy here. You not even know if at this moment you're really using PostgreSQL).

        """

        # Database user name from the configuration file.
        username   = self.getConfiguration( 'database', 'user' )

        # This command only list the tables from the database.
        command = 'psql -U ' + username + " -c '\dt'"

        result = subprocess.call( command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Zero means (from the subprocess package) the command could be executed without errors.
        if result == 0:
            return True
        else:
            return False


    def checkYouHaveTheRightTables( self ):
        """
        This method won't check foreign keys, tables columns nor any kind of contraints.

        It only check if you have the right table names in you database.

        And if you don't have the exacly expected tables, you're screwed. Call for help.

        Read the code comments in this method to understand better what's happening.

        """

        expectedTables = []
        foundTables    = []

        # Fill a list containing all the expected tables from self.files dictionary.
        # And self.files is THE true in this class.
        for myFile in self.files:
            expectedTables.append( myFile['table'] )

        # Just get data to be possible to enter into postgresql.
        username   = self.getConfiguration( 'database', 'user' )

        # Get all tables from the EXPECTED relational database you've created.
        sqlTables = "SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';"

        # Actual get the data said above executing the 'psql' command.
        p = subprocess.Popen(["psql", '-U', 'kegg2017', '-t', '-c', sqlTables ], stdout=subprocess.PIPE)

        # Store the result of the command above.
        out, err = p.communicate()

        # The result is not cool, we have to split that in lines.
        tables = out.split('\n')

        # And we have to remove empty lines (the result has it!).
        reRemoveEmptyLines = re.compile('^$')

        # Iterate through the result tables from the actual, real, relational database you've created.
        for t in tables:
            # Actual ignore empty lines.
            if reRemoveEmptyLines.search( t ):
                continue

            # Remove blank spaces and weird useless '.' characters.
            tableName = re.sub( '\ ', '', t )
            tableName = re.sub( '\.', '', tableName )

            # Now we fill the found tables from your relational database.
            foundTables.append( tableName )


        # TODO: fix lack of expected tables.
        # -------------------------------------------------------------------------------------------
        # Some table doesn't belong to the Loader but it exists...
        # It means tables that have to be populated manually or tables you know are
        # critical but you don't populate those using this Loader.
        # If you're doing smart things in your relational database, this thing have to 
        # be concerned.
        expectedTables.append( 'source_databases' )    # this goes manually.
        expectedTables.append( 'protein_pdbs' )        # this is important and will be filled later.
        expectedTables.append( 'ec_reaction_classes' ) # this goes manually.
        expectedTables.append( 'clusters' )            # this goes by outside process.
        expectedTables.append( 'clustering_methods' )  # this goes by outside process.
        # END of not fancy workaround. But loaders... come on... you know... loaders... 
        # If you're a developer, you're horrified. If you're a database administrator
        # you're horrified. But if you are a guy that deals with loaders through big data
        # well... you know...
        # -------------------------------------------------------------------------------------------

        # Remove possible duplications (we never know).
        expectedTables = set(expectedTables)
        expectedTables = list(expectedTables)

        # Oh my god... if all the expected tables are exacly the same as the tables we're going
        # to fill using this class... everything is so fine and cool!!
        # It means you created a database with exacly the same tables this class expect. Congratulations!!
        if set(foundTables) == set(expectedTables):
            return True
        else:
            return False


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
        """
        This is the serious business.

        This methos insert into the relational database all the data caught from KeggReader package.

        """

        if not self.checkPsqlCanExecuteCommand():
            print( "ERROR:")
            print( "I cannot execute 'psql' command properly, so I won't try to load data.")
            print( "Maybe it means you don't have a properly $HOME/.pgpass correct file." )
            print( "Try to create in you $USER directory a file .pgpass with the following data: ")
            print( "localhost:5432:kegg2017:darkmatter" )
            print( "BUT it's only a suggestion. Call your database administrator to know what it is." )
            sys.exit()

        if not self.checkYouHaveTheRightTables():
            print( "ERROR:")
            print( "You don't have the correct tables created in you PostgreSQL database.")
            print( "Maybe it means you don't execute the correct restore procedure using the 'sql' file provided by this package." )
            print( "Maybe there's a different set of tables in you database. ")
            print( "You have to have the exacly table names expected by this module, no more table names, no less table names.")
            print( "Check if you created any kind of test table or something.")
            print( "Again, you have to have the exactly set of tables expected by this module.")
            print( "Here's the list: "  )
            for myTable in self.files:
                print( myTable['table'] )

            print( '--------------------------------------------------------------------------------' )
            print( "\n" )
            sys.exit()


        # Load PostgreSQL database logging data.
        dataSource = self.getConfiguration( 'directories', 'inserts' )
        username   = self.getConfiguration( 'database', 'user' )
    
        # ------------------------------------------------------------------------ #
        # ---------------- THAT'S THE STUFF WE'RE LOOKING FOR -------------------- #
        # ------------------------------------------------------------------------ #
        # This part of the code actual inserts the data into relational database   #
        # ------------------------------------------------------------------------ #
        # Load each data file into relational database.
        for loadFile in self.files:

            # Only print into the screen what table is being populated.
            pprint.pprint( '-----------------------------------------------' )
            pprint.pprint( loadFile['file'] )
            pprint.pprint( '-----------------------------------------------' )
            print( "\n" )
            # END of telling what's happening.

            # Find the source insert file data.
            fileToLoad = dataSource + '/' + loadFile['file'] 

            # Find the relational database table name to be filled.
            table = loadFile['table']

            # Columns names are being put together as a list of columns (psql needed).
            columns = ','.join( loadFile['columns'] )

            # Actual execute the command that inserts the data into relational database.
            process = subprocess.Popen( "psql -U " + username + " -c \"\copy " + table + "(" + columns + ") from \'" + fileToLoad + "\';\"", shell=True )

            # Things got crazy here. Some table delays a lot to be inserted and the process keep going overwhelming the next process.
            # So we wait to make sure the tables order insertions are correct.
            process.wait()
        # ------------------------------------------------------------------------ #
        # ---------------- END OF THE POPULATING PROCESS ------------------------- #
        # ------------------------------------------------------------------------ #


