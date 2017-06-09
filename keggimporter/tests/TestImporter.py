import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from Importer import *
import re


class TestImporter( unittest.TestCase ):

    def setUp( self ):
        self.imp = Importer()

    def test_startImporter( self ):

        self.imp.startImporter()


    def test_getConfiguration( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )
        
        config = self.imp.getConfiguration( 'directories', 'inserts' )
        expectedConfig = './fixtures/inserts'

        self.assertEquals( config, expectedConfig )

    def test_openInsertFile( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        result = self.imp.openInsertFile( 'remove_this_file' )

        self.assertTrue( type( result ) is file )

        result.close()
 

    def test_nextPrimaryKey( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        result = self.imp.nextPrimaryKey( 'test' )

        self.assertEquals( result, 1 )

        result = self.imp.nextPrimaryKey( 'test' )

        self.assertEquals( result, 2 )

        result = self.imp.nextPrimaryKey( 'test' )

        self.assertEquals( result, 3 )


    def test_writeFile( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        f = open('./fixtures/remove_this_thing', 'a')

        result = self.imp.writeFile( f, 'test_table', [ 'bla', 'ble', 'bli' ] )

        self.assertEquals( result, 1 )

        result = self.imp.writeFile( f, 'test_table', [ 'bla', 'ble', 'bli' ] )

        self.assertEquals( result, 2 )

        result = self.imp.writeFile( f, 'test_table', [ 'bla', 'ble', 'bli' ] )

        self.assertEquals( result, 3 )


    def test_write_importer_files( self ):

        self.imp.importerPathway.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.importerPathway.setConfigurationFile( confFile )
 
        self.imp.importerEc.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.importerEc.setConfigurationFile( confFile )

        self.imp.importerOrganism.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.importerOrganism.setConfigurationFile( confFile )

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )
 
        self.imp.writeTaxonomies()
        self.imp.writePathways()
        self.imp.writeEcs()
        self.imp.writeOrganisms()
        self.imp.writeProteins()
        self.imp.writeProteinRelations()
        self.imp.writeOrganismTaxonomies()
        self.imp.writeProteinAccessions()
        self.imp.writeEcMaps()


        expectedFiles = [
            'accessionsInsert.psql',
            'organismTaxonomiesInsert.psql',
            'proteinMapsInsert.psql',
            'ecMapsInsert.psql',
            'pathwayClassesInsert.psql',
            'proteinsInsert.psql',
            'ecsInsert.psql',
            'pathwayNamesInsert.psql',
            'organismEcsInsert.psql',
            'pathwaySuperClassesInsert.psql',
            'taxonomiesInsert.psql',
            'organismMapsInsert.psql',
            'proteinAccessionsInsert.psql',
            'organismsInsert.psql',
            'proteinEcsInsert.psql'
            ]

        for insertFile in expectedFiles:
            f = open( './fixtures/inserts/' + insertFile )
            self.assertTrue( type( f ) is file ) 

            count = 0
            for line in f:
                count += 1

            # Random number greater than 1
            if count == 10:
                break

            # Random number around an expected minimum amount of records.
            # Empty files will raise an error (what we want to caught).
            if count < 5:
                print( 'EMPTY FILE: ' + insertFile )

            self.assertTrue( count > 5 )

            f.close()





if __name__ == "__main__":
    unittest.main()
