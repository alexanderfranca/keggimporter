import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from ImporterPathway import *
import re


class TestImporterPathway( unittest.TestCase ):

    def setUp( self ):
        self.imp = ImporterPathway()

    def test_startImporter( self ):

        self.imp.startImporter()


    def test_getConfiguration( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )
        
        config = self.imp.getConfiguration( 'directories', 'inserts' )
        expectedConfig = './fixtures/inserts'

        self.assertEquals( config, expectedConfig )


    def test_openPathwaySuperClassFile( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        result = self.imp.openPathwaySuperClassesFile() 

        self.assertTrue( type( result ) is file )


    def test_nextPathwaySuperClassPrimaryKey( self ):

        expected = 3

        # 1
        self.imp.nextPathwaySuperClassPrimaryKey()

        # 2
        self.imp.nextPathwaySuperClassPrimaryKey()

        # 3
        result = self.imp.nextPathwaySuperClassPrimaryKey()

        self.assertEquals( result, expected ) 


    def test_openPathwayClassFile( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        result = self.imp.openPathwayClassesFile() 

        self.assertTrue( type( result ) is file )



    def test_nextPathwayClassPrimaryKey( self ):

        expected = 3

        # 1
        self.imp.nextPathwayClassPrimaryKey()

        # 2
        self.imp.nextPathwayClassPrimaryKey()

        # 3
        result = self.imp.nextPathwayClassPrimaryKey()

        self.assertEquals( result, expected ) 


    def test_openPathwayNameFile( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        result = self.imp.openPathwayNamesFile() 

        self.assertTrue( type( result ) is file )


    def test_nextPathwayNamePrimaryKey( self ):

        expected = 3

        # 1
        self.imp.nextPathwayNamePrimaryKey()

        # 2
        self.imp.nextPathwayNamePrimaryKey()

        # 3
        result = self.imp.nextPathwayNamePrimaryKey()

        self.assertEquals( result, expected ) 



    def test_writePathways( self ):

        self.imp.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        self.imp.writePathways()


if __name__ == "__main__":
    unittest.main()
