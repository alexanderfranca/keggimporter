import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from Loader import *
import re


class TestLoader( unittest.TestCase ):

    def setUp( self ):
        self.imp = Loader()

    def test_start( self ):

        self.imp.start()

    def test_getConfiguration( self ):

        self.imp.start() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )
        
        config = self.imp.getConfiguration( 'directories', 'inserts' )
        expectedConfig = './fixtures/inserts'

        self.assertEquals( config, expectedConfig )

    def test_checkPsqlCanExecuteCommand( self ):

        self.imp.start() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        result = self.imp.checkPsqlCanExecuteCommand()

        self.assertTrue( result )

    def test_checkYouHaveTheRightTables( self ):

        self.imp.start() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )

        result = self.imp.checkYouHaveTheRightTables()

        self.assertTrue( result )

    def test_loadFiles( self ):

        self.imp.start() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )
 
        self.imp.loadFiles()


if __name__ == "__main__":
    unittest.main()
