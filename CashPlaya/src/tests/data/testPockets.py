'''
Created on May 2, 2013

@author: moz
'''
import unittest
from data.pockets import pockets
from data.point import point
import numpy

offsetPoint = point( 10, 20 )
gridsize = point(7 ,7)
pocketSize = 40
smallBlackImage = numpy.zeros((pocketSize, pocketSize, 3), numpy.float32)
bigWhiteImage = numpy.zeros((pocketSize*10, pocketSize*10, 3), numpy.float32)
bigWhiteImage[:,:] = (255,255,255)      # (B, G, R)
bigBlackImage = numpy.zeros((pocketSize*10, pocketSize*10, 3), numpy.float32)

emptyImageList = {}
for col in range( 0, gridsize.x):
    for row in range( 0, gridsize.y):
        emptyImageList[(col, row)] = smallBlackImage

class Test(unittest.TestCase):


    def testPockets(self):
        p = pockets( offsetPoint, emptyImageList )
        self.assertEqual( p.pointTopLeft, offsetPoint )
        self.assertEqual( p.pointBottomRight, offsetPoint+7*point(pocketSize, pocketSize) - point( 1, 1 ) )    
        pass

    def testGetContent(self):
        p = pockets( offsetPoint, emptyImageList )
        self.assertTrue( p.processImage( bigBlackImage ) )
        self.assertTrue( p.isEmpty(2,2) )        
        
    def testShowPocketBoundaries(self):
        p = pockets( offsetPoint, emptyImageList )
        color = (0, 0, 255)
        
        bigImage = numpy.zeros((pocketSize*10, pocketSize*10, 3), numpy.float32)
        p.ShowPocketBoundaries( color, bigImage )
        
        # yes, x and y are inverted...
        self.assertEqual( bigImage[ offsetPoint.y, offsetPoint.x ][0], color[0] )
        self.assertEqual( bigImage[ offsetPoint.y, offsetPoint.x ][1], color[1] )
        self.assertEqual( bigImage[ offsetPoint.y, offsetPoint.x ][2], color[2] )
        
    def testGetImage(self):
        p = pockets( offsetPoint, emptyImageList )
        self.assertTrue( p.processImage( bigBlackImage ) )
        self.assertTrue( numpy.array_equal( p.getImage(2,2), smallBlackImage ) )
        
    def testShowPocketValues(self):
        p = pockets( offsetPoint, emptyImageList )
        color = (0, 0, 255)
        
        bigImage = numpy.zeros((pocketSize*10, pocketSize*10, 3), numpy.float32)
        p.ShowPocketValues( color, bigImage )

    def testGetSetValue(self):
        p = pockets( offsetPoint, emptyImageList )
        self.assertTrue( p.processImage( bigBlackImage ) )
        p.setValue(2,2, 'X')
        self.assertEqual( p.getValue( 2, 2 ), 'X' )
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPockets']
    unittest.main()