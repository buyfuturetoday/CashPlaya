'''
Created on May 4, 2013

@author: moz
'''
import unittest
from data.point import point
from data.ScoreBoard import ScoreBoard
from data.ItemList import ItemList
import cv2

offsetPoint = point( 10, 20 )
il = ItemList( 'data/digits', "digit_%d.bmp")
digit = cv2.imread( 'data/digits/digit_1.bmp' )

class Test(unittest.TestCase):


    def testScoreBoard(self):
        sb = ScoreBoard( offsetPoint, il )
        self.assertEqual(sb.pointTopLeft, offsetPoint )

    def testReadScore(self):
        sb = ScoreBoard( offsetPoint, il )
#        sb.Read
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testScoreBoard']
    unittest.main()