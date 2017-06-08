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

        self.imp.importerPathway.startImporter() 
        confFile = './fixtures/keggimporter.conf'
        self.imp.importerPathway.setConfigurationFile( confFile )
 
        #self.imp.importerProtein.startImporter() 
        #confFile = './fixtures/keggimporter.conf'
        #self.imp.importerProtein.setConfigurationFile( confFile )
        
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




if __name__ == "__main__":
    unittest.main()
