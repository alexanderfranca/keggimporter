import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from ImporterEc import *
from keggreader import *
import re


class TestImporterEc( unittest.TestCase ):

    def setUp( self ):
        reader = KeggReader()

        self.imp = ImporterEc(
                                destination_file='./fixtures/inserts/ecsInsert.psql',
                                keggreader=reader,
                            )

    def test_next_ec_primary_key( self ):

        expected = 3

        # 1
        self.imp.next_ec_primary_key()

        # 2
        self.imp.next_ec_primary_key()

        # 3
        result = self.imp.next_ec_primary_key()

        self.assertEquals( result, expected ) 


    def test_write_ecs( self ):

        self.imp.write_ecs()


if __name__ == "__main__":
    unittest.main()
