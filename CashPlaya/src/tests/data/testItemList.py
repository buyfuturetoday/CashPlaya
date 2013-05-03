'''
Created on May 3, 2013

@author: moz
'''
import unittest

from data.ItemList import ItemList


itemcount = 3
itempath = 'testdata/items'

class Test(unittest.TestCase):


    def testItemList(self):
        il = ItemList( itempath )
        self.assertEqual( il.count, itemcount )
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testItemList']
    unittest.main()