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
        
    def testPointEqual(self):
        p1 = point( 3,4 )
        p2 = point( 3,4 )
        self.assertTrue(p1==p2)
    
    def testPointAdd(self):
        a,b,c,d = 1,2,3,4
        p1 = point( a,b)
        p2 = point( c,d)
        self.assertEqual(p1+p2, point(a+c, b+d ) )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()