import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from ImporterTaxonomy import *
import re


class TestImporterTaxonomy( unittest.TestCase ):

    def setUp( self ):
        self.imp = ImporterTaxonomy()

    def test_startImporter( self ):

        self.imp.startImporter()


    def test_getConfiguration( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )
        
        config = self.imp.getConfiguration( 'directories', 'inserts' )
        expectedConfig = './fixtures/inserts'

        self.assertEquals( config, expectedConfig )


    def test_openTaxonomyFile( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        result = self.imp.openTaxonomiesFile() 

        self.assertTrue( type( result ) is file )

    def test_nextTaxonomyPrimaryKey( self ):

        expected = 3

        # 1
        self.imp.nextTaxonomyPrimaryKey()

        # 2
        self.imp.nextTaxonomyPrimaryKey()

        # 3
        result = self.imp.nextTaxonomyPrimaryKey()

        self.assertEquals( result, expected ) 


    def test_writeTaxonomies( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        self.imp.writeTaxonomies()


if __name__ == "__main__":
    unittest.main()
