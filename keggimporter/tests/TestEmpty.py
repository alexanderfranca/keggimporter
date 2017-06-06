import sys
import os
sys.path.insert(0,  os.getcwd() + '/../')
import unittest
from Empty import *
import re


class TestEmpty( unittest.TestCase ):

    def setUp( self ):
        self.empty = Empty()


if __name__ == "__main__":
    unittest.main()
