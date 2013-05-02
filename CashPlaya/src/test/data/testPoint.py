'''
Created on May 2, 2013

@author: moz
'''
import unittest
from data.point import point


class Test(unittest.TestCase):


    def testPoint(self):
        p = point( 1,2 )
        self.assertEqual( p.x, 1)
        self.assertEqual( p.y, 2)
        pass

    def testPointTupple(self):
        p = point( 3, 4 )
        self.assertEqual(p.tupple, (3,4) )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()