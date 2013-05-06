'''
Created on May 4, 2013

@author: moz
'''
import unittest
from data.point import point
from data.ScoreBoard import ScoreBoard
from data.ItemList import ItemList
import cv2
import numpy

offsetPoint = point( 10, 20 )
il = ItemList( 'testdata/digits', "digit_%d.png")
il.setThreshold(0.8)
digit = cv2.imread( 'testdata/digits/digit_0.png' )
assert( digit is not None )

scoreboard_A = cv2.imread( 'testdata/digits/ScoreBoard_369350.png' )
scoreboard_A_score = 369350
assert( scoreboard_A is not None )
scoreboard_B = cv2.imread( 'testdata/digits/ScoreBoard_105.png' )
scoreboard_B_score = 105
assert( scoreboard_B is not None )
scoreboard_C = cv2.imread( 'testdata/digits/ScoreBoard_248010.png' )
scoreboard_C_score = 248010
assert( scoreboard_C is not None )
scoreboard_D = cv2.imread( 'testdata/digits/ScoreBoard_177000.png' )
scoreboard_D_score = 177000
assert( scoreboard_D is not None )

class Test(unittest.TestCase):


    def testScoreBoard(self):
        sb = ScoreBoard( offsetPoint, il )
        self.assertEqual(sb.pointTopLeft, offsetPoint )

    def testShowBoundaries(self):
        color = (0, 0, 255)        
        bigImage = numpy.zeros((100, 100, 3), numpy.float32)
        
        sb = ScoreBoard( offsetPoint, il )
        sb.ShowBoundary(color, bigImage)
         
    def testReadScoreA(self):
        sb = ScoreBoard( point( 0,0 ), il )
        scoreread = sb.ReadScore( scoreboard_A )
 
#         sb.ShowBoundary((0,0,255), scoreboard_A)
#         cv2.imshow("A", scoreboard_A)
#         cv2.waitKey()
         
        self.assertEqual(scoreboard_A_score, scoreread)
          
    def testReadScoreB(self):
        sb = ScoreBoard( point( 0,0 ), il )
        scoreread = sb.ReadScore( scoreboard_B )
  
#         sb.ShowBoundary((0,0,255), scoreboard_B)
#         cv2.imshow("B", scoreboard_B)
#         cv2.waitKey()
          
        self.assertEqual(scoreboard_B_score, scoreread)   
         
    def testReadScoreC(self):
        sb = ScoreBoard( point( 0,0 ), il )
        scoreread = sb.ReadScore( scoreboard_C )
        self.assertEqual(scoreboard_C_score, scoreread)   
           
    def testReadScoreD(self):
        sb = ScoreBoard( point( 0,0 ), il )
        scoreread = sb.ReadScore( scoreboard_D )
  
#         sb.ShowBoundary((0,0,255), scoreboard_D)
#         cv2.imshow("B", scoreboard_D)
#         cv2.imwrite("scoreB.png", scoreboard_D)
#         cv2.waitKey()
         
        self.assertEqual(scoreboard_D_score, scoreread)   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testScoreBoard']
    unittest.main()