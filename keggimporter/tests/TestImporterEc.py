import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from ImporterEc import *
import re


class TestImporterEc( unittest.TestCase ):

    def setUp( self ):
        self.imp = ImporterEc()

    def test_startImporter( self ):

        self.imp.startImporter()


    def test_getConfiguration( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )
        
        config = self.imp.getConfiguration( 'directories', 'inserts' )
        expectedConfig = './fixtures/inserts'

        self.assertEquals( config, expectedConfig )


    def test_openEcFile( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        result = self.imp.openEcsFile() 

        self.assertTrue( type( result ) is file )

    def test_nextEcPrimaryKey( self ):

        expected = 3

        # 1
        self.imp.nextEcPrimaryKey()

        # 2
        self.imp.nextEcPrimaryKey()

        # 3
        result = self.imp.nextEcPrimaryKey()

        self.assertEquals( result, expected ) 


    def test_writeEcs( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        self.imp.writeEcs()


if __name__ == "__main__":
    unittest.main()
