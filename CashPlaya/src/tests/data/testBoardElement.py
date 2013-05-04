'''
Created on May 4, 2013

@author: moz
'''
import unittest
from data.point import point
from data.BoardElement import BoardElement
import numpy

offsetPoint = point( 10, 20 )
size = point( 35, 45 )
bigBlackImage = numpy.zeros((size.x*10, size.y*10, 3), numpy.float32)

class Test(unittest.TestCase):


    def testBoardElement(self):
        be = BoardElement( offsetPoint, size )
        self.assertEqual( be.pointTopLeft, offsetPoint )
        self.assertEqual( be.pointBottomRight, offsetPoint+size+point(-1, -1) )    
      
    def testDrawBoundary(self):
        color = (0, 0, 255)
        p = BoardElement( offsetPoint, size )
        
        bigImage = numpy.zeros((size.x*10, size.y*10, 3), numpy.float32)
        p.ShowBoundary( color, bigImage )        

        # yes, x and y are inverted...
        self.assertEqual( bigImage[ offsetPoint.y, offsetPoint.x ][0], color[0] )
        self.assertEqual( bigImage[ offsetPoint.y, offsetPoint.x ][1], color[1] )
        self.assertEqual( bigImage[ offsetPoint.y, offsetPoint.x ][2], color[2] )

    def testSetValue(self):
        bigImage = numpy.zeros((size.x*10, size.y*10, 3), numpy.float32)
        
        p = BoardElement( offsetPoint, size )
        p.setValue( 'X' )
        self.assertEqual( p.value, 'X' )
        
        p.ShowValue( (0,0,255), bigImage )

    def testGetImage(self):
        be = BoardElement( offsetPoint, size )
        img = be.getImage( bigBlackImage )
        self.assertEqual( (img.shape[1], img.shape[0]), size.tupple ) 

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testBoardElement']
    unittest.main()