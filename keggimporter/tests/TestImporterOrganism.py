import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from ImporterOrganism import *
import re


class TestImporterOrganism( unittest.TestCase ):

    def setUp( self ):
        self.imp = ImporterOrganism()

    def test_startImporter( self ):

        self.imp.startImporter()


    def test_getConfiguration( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )
        
        config = self.imp.getConfiguration( 'directories', 'inserts' )
        expectedConfig = './fixtures/inserts'

        self.assertEquals( config, expectedConfig )


    def test_openOrganismFile( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        result = self.imp.openOrganismsFile() 

        self.assertTrue( type( result ) is file )

    def test_nextOrganismPrimaryKey( self ):

        expected = 3

        # 1
        self.imp.nextOrganismPrimaryKey()

        # 2
        self.imp.nextOrganismPrimaryKey()

        # 3
        result = self.imp.nextOrganismPrimaryKey()

        self.assertEquals( result, expected ) 


    def test_writeOrganisms( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        self.imp.writeOrganisms()


if __name__ == "__main__":
    unittest.main()
