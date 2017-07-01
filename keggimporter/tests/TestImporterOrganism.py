import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from ImporterOrganism import *
from keggreader import *
import re


class TestImporterOrganism( unittest.TestCase ):

    def setUp( self ):

        reader = KeggReader()

        self.imp = ImporterOrganism(
                                    destination_file='./fixtures/inserts/organismsInsert.psql',
                                    keggreader=reader,
                                    )

    def test_next_organism_primary_key( self ):

        expected = 3

        # 1
        self.imp.next_organism_primary_key()

        # 2
        self.imp.next_organism_primary_key()

        # 3
        result = self.imp.next_organism_primary_key()

        self.assertEquals( result, expected ) 


    def test_write_organisms( self ):

        self.imp.write_organisms()


if __name__ == "__main__":
    unittest.main()
