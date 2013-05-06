'''
Created on May 3, 2013

@author: moz
'''
import unittest

from data.ItemList import ItemList
import cv2

itempath = 'testdata/items'

# A list - normal operation
itemcount = 3

# B list - with gap
filepattern_B="item_B_%02d.bmp"
itemcount_B = 2


class Test(unittest.TestCase):


    def testItemList(self):
        il = ItemList( itempath )
        self.assertEqual( il.count, itemcount )
        pass
    
    def testItemListwithGap(self):
        il = ItemList( itempath, filepattern=filepattern_B )
        self.assertEqual( il.count, itemcount_B )
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

    def testFindItemThreshold(self):
        il = ItemList( itempath )
        imToFind = cv2.imread( "%s/item_00.bmp"% itempath)
        itemno = il.findItem( imToFind )
        self.assertEqual( itemno, 0 )
        
        imToFind = cv2.imread( "%s/item_00_almost.bmp"% itempath)
        il.setThreshold( 0.1 )
        itemno = il.findItem( imToFind )
        self.assertEqual( itemno, 0 )
        
    def testGetItemInfo(self):
        il = ItemList( itempath )
        imToFind = cv2.imread( "%s/item_00_almost.bmp"% itempath)
        il.setThreshold( 0.1 )
        il.findItem( imToFind )
        info = il.getLastResult()
        self.assertEqual( info[0], (0.9475897550582886, 0.9475897550582886, (0, 0), (0, 0)) )
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testItemList']
    unittest.main()