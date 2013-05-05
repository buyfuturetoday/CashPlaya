'''
Created on May 4, 2013

@author: moz
'''
import unittest
from data.point import point
from data.Digit import Digit

offset = point( 3, 7)
size = point( 15, 30 )

class Test(unittest.TestCase):


    def testDigit(self):
        d = Digit( offset, size  )
        self.assertNotEqual(d, None)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDigit']
    unittest.main()