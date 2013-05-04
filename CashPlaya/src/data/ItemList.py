# links:
# - http://stackoverflow.com/questions/7589012/combining-two-images-with-opencv

import os
import cv2
import numpy

class ItemList(object):
        
    def __init__(self, itempath, filepattern = "item_%02d.bmp"):
        self.path = itempath
        self.filepattern = filepattern
        self.initImages( )
    
    def initImages(self):
        itemcounter = 0
        images = []
        width = 0
        
        # loop until no more files
        while True:
            filename = os.path.join( self.path, self.filepattern%itemcounter)

            if not os.path.isfile( filename ):
                break

            images.append( cv2.imread( filename ) )
            itemcounter = itemcounter + 1
            
        # and save the result        
        self.imagecount = itemcounter
        self.itemsize = width
        self.allImages = images

    @property
    def count(self):
        return self.imagecount

    
    def findItem(self, imToFind):
        maxval = 0
        maximg = 0
        for i in range( 0, len(self.allImages)):
            result = cv2.matchTemplate(self.allImages[i], imToFind,cv2.TM_CCORR_NORMED)
            if maxval < result[0]:
                maxval = result[0]
                maximg = i
    
        # TODO: magic val. threshold value for acceptance    
        if maxval < 0.99:
            return None
    
        return maximg
    
    
    



