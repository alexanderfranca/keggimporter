import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from ImporterProtein import *
import re


class TestImporterProtein( unittest.TestCase ):

    def setUp( self ):
        self.imp = ImporterProtein()

    def test_startImporter( self ):

        self.imp.startImporter()


    def test_getConfiguration( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )
        
        config = self.imp.getConfiguration( 'directories', 'inserts' )
        expectedConfig = './fixtures/inserts'

        self.assertEquals( config, expectedConfig )




    def test_openProteinFile( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        result = self.imp.openProteinsFile() 

        self.assertTrue( type( result ) is file )

    def test_nextProteinPrimaryKey( self ):

        expected = 3

        # 1
        self.imp.nextProteinPrimaryKey()

        # 2
        self.imp.nextProteinPrimaryKey()

        # 3
        result = self.imp.nextProteinPrimaryKey()

        self.assertEquals( result, expected ) 

    def test_writeProteins( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        self.imp.writeProteins()



if __name__ == "__main__":
    unittest.main()
