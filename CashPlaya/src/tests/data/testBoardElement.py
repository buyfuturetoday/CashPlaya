'''
Created on May 4, 2013

@author: moz
'''
import unittest
from data.point import point
from data.BoardElement import BoardElement

offsetPoint = point( 10, 20 )
size = point( 35, 45 )

class Test(unittest.TestCase):


    def testBoardElement(self):
        be = BoardElement( offsetPoint, size )
        self.assertEqual( be.pointTopLeft, offsetPoint )
        self.assertEqual( be.pointBottomRight, offsetPoint+size+point(-1, -1) )    
      


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBoardElement']
    unittest.main()