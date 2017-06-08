import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from Loader import *
import re


class TestLoader( unittest.TestCase ):

    def setUp( self ):
        self.imp = Importer()

    def test_start( self ):

        self.imp.start()

    def test_getConfiguration( self ):

        self.imp.start() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )
        
        config = self.imp.getConfiguration( 'directories', 'inserts' )
        expectedConfig = './fixtures/inserts'

        self.assertEquals( config, expectedConfig )


    def test_loadFiles( self ):

        self.imp.start() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.setConfigurationFile( confFile )
 
        self.imp.loadFiles()

        #pprint.pprint( self.imp.files )


if __name__ == "__main__":
    unittest.main()
