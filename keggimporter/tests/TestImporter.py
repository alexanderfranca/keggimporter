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


    def test_writeProteins( self ):

        self.imp.importerProtein.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.importerProtein.setConfigurationFile( confFile )
        
        self.imp.importerEc.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.importerEc.setConfigurationFile( confFile )
 

        self.imp.writeProteins()




if __name__ == "__main__":
    unittest.main()
