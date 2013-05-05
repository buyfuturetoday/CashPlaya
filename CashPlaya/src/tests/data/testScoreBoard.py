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
il = ItemList( 'data/digits', "digit_%d.bmp")
digit = cv2.imread( 'data/digits/digit_1.bmp' )

scoreboard_A = cv2.imread( 'data/digits/scoreboard_369350.bmp' )
scoreboard_A_score = 369350

class Test(unittest.TestCase):


    def testScoreBoard(self):
        sb = ScoreBoard( offsetPoint, il )
        self.assertEqual(sb.pointTopLeft, offsetPoint )

    def testShowBoundaries(self):
        color = (0, 0, 255)        
        bigImage = numpy.zeros((100, 100, 3), numpy.float32)
        
        sb = ScoreBoard( offsetPoint, il )
        sb.ShowBoundary(color, bigImage)
        
#     def testReadScore(self):
#         
#         sb = ScoreBoard( point( 3,2 ), il )
#         sb.ReadScore( scoreboard_A )
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testScoreBoard']
    unittest.main()