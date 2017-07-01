import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from keggreader import *
from ImporterPathway import *
import re


class TestImporterPathway( unittest.TestCase ):

    def setUp( self ):

        reader = KeggReader()

        self.imp = ImporterPathway(
                                    pathway_super_class_file='./fixtures/inserts/pathwaySuperClassesInsert.psql',
                                    pathway_class_file='./fixtures/inserts/pathwayClassesInsert.psql',
                                    pathway_file='./fixtures/inserts/pathwayNamesInsert.psql',
                                    keggreader=reader, 
                                    )

    def test_next_pathway_super_class_primary_key( self ):

        expected = 3

        # 1
        self.imp.next_pathway_super_class_primary_key()

        # 2
        self.imp.next_pathway_super_class_primary_key()

        # 3
        result = self.imp.next_pathway_super_class_primary_key()

        self.assertEquals( result, expected ) 


    def test_next_pathway_class_primary_key( self ):

        expected = 3

        # 1
        self.imp.next_pathway_class_primary_key()

        # 2
        self.imp.next_pathway_class_primary_key()

        # 3
        result = self.imp.next_pathway_class_primary_key()

        self.assertEquals( result, expected ) 

    def test_next_pathway_name_primary_key( self ):

        expected = 3

        # 1
        self.imp.next_pathway_name_primary_key()

        # 2
        self.imp.next_pathway_name_primary_key()

        # 3
        result = self.imp.next_pathway_name_primary_key()

        self.assertEquals( result, expected ) 

    def test_write_pathways( self ):

        self.imp.write_pathways()


if __name__ == "__main__":
    unittest.main()
