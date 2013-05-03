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
smallBlackImage = numpy.zeros((pocketSize-1, pocketSize-1, 3), numpy.float32)
bigWhiteImage = numpy.zeros((pocketSize*10, pocketSize*10, 3), numpy.float32)
bigWhiteImage[:,:] = (255,255,255)      # (B, G, R)
bigBlackImage = numpy.zeros((pocketSize*10, pocketSize*10, 3), numpy.float32)

class Test(unittest.TestCase):


    def testPockets(self):
        p = pockets( offsetPoint )
        self.assertEqual( p.pointTopLeft, offsetPoint )
        self.assertEqual( p.pointBottomRight, offsetPoint+7*point(pocketSize, pocketSize) - point( 1, 1 ) )    
        pass

    def testGetContent(self):
        p = pockets( offsetPoint )
        self.assertTrue( p.processImage( bigBlackImage ) )
        self.assertTrue( p.isEmpty(2,2) )
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPockets']
    unittest.main()