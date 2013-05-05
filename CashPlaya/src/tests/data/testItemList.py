'''
Created on May 3, 2013

@author: moz
'''
import unittest

from data.ItemList import ItemList
import cv2


itemcount = 3
itempath = 'testdata/items'

class Test(unittest.TestCase):


    def testItemList(self):
        il = ItemList( itempath )
        self.assertEqual( il.count, itemcount )
        pass

    def testFindItem(self):
        il = ItemList( itempath )

        imToFind = cv2.imread( "%s/item_00.bmp"% itempath)
        itemno = il.findItem( imToFind )
        self.assertEqual( itemno, 0 )

        imToFind = cv2.imread( "%s/item_02.bmp"% itempath)
        itemno = il.findItem( imToFind )
        self.assertEqual( itemno, 2 )

    def testGetSize(self):
        il = ItemList( itempath )
        self.assertEqual( (39, 39), il.getSize( 0 ))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testItemList']
    unittest.main()