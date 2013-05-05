'''
Created on May 4, 2013

@author: moz
'''
import unittest
from data.point import point
from data.Digit import Digit

offset = point( 3, 7)

class Test(unittest.TestCase):


    def testDigit(self):
        d = Digit( offset )
        self.assertNotEqual(d, None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDigit']
    unittest.main()