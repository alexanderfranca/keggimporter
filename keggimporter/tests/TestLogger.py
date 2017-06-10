import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from Logger import *
import re


class TestLogger( unittest.TestCase ):

    def setUp( self ):
        self.log = Logger()

    def test_setConfigurationFile( self ):

        confFile = './fixtures/keggimporter.conf'
        self.log.setConfigurationFile( confFile )
        
        config = self.log.getConfiguration( 'log', 'info' )

        expectedConfig = './fixtures/log/keggimporter.log'

        self.assertEquals( config, expectedConfig )

    def test_createLogSystem( self ):

        confFile = './fixtures/keggimporter.conf'
        self.log.setConfigurationFile( confFile )
        
        logger = self.log.createLogSystem()

        logger.info( 'a test string to be logged' ) 

        expectedFile = './fixtures/log/keggimporter.log'

        f = open( expectedFile )

        self.assertTrue( type( f ) is file )


if __name__ == "__main__":
    unittest.main()
