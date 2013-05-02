'''
Created on May 2, 2013

@author: moz
'''
import unittest
from data. point import point
from data.pocket import pocket
import numpy
import cv2

# test data
offsetPoint = point( 10, 20 )
pocketSize = 40
smallBlackImage = numpy.zeros((pocketSize-1, pocketSize-1, 3), numpy.float32)
bigWhiteImage = numpy.zeros((pocketSize*10, pocketSize*10, 3), numpy.float32)
bigWhiteImage[:,:] = (255,255,255)      # (B, G, R)
bigBlackImage = numpy.zeros((pocketSize*10, pocketSize*10, 3), numpy.float32)
#bigBlackImage[:,:] = (0,0,0)      # (B, G, R)

# # debug stuff
# cv2.imshow( "bigWhiteImage", bigWhiteImage )
# cv2.imshow( "bigBlackImage", bigBlackImage )
# cv2.imshow( "emptyImage", emptyImage)
# cv2.waitKey()

class Test(unittest.TestCase):


    def testPocket(self):
        p = pocket( offsetPoint, smallBlackImage )
        self.assertEqual( p.pointTopLeft, offsetPoint )
        self.assertEqual( p.pointBottomRight, offsetPoint+point(pocketSize-1, pocketSize-1) )        
        pass

    def testIsEmpty(self):
        p = pocket( offsetPoint, smallBlackImage )
        # it is empty if "emptyimage" is located at the offset, ie. all black
        self.assertTrue( p.isEmpty( bigBlackImage ) )
        self.assertFalse( p.isEmpty( bigWhiteImage ) )
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPocket']
    unittest.main()