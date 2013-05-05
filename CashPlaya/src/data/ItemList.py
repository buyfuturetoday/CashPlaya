# links:
# - http://stackoverflow.com/questions/7589012/combining-two-images-with-opencv

import os
import cv2
import numpy
import sys

class ItemList(object):
    ''' contains a list of images loaded from disk. 
        To be used to select the best match of an image
        '''
    _findThreshold = 0.99 # very matches are default
        
    def __init__(self, itempath, filepattern = "item_%02d.bmp"):
        ''' inits the class
        @param itempath: the directory containing the image files
        @param filepattern: the specific file names - must include a single %d for the internal counter.
        '''
        self.path = itempath
        self.filepattern = filepattern
        self.initImages( )
    
    def initImages(self):
        ''' Initializes the images by loading from disk.
            Based on a count and a file pattern, when no more image files are found, it stops loading
            eg. img00, img01, img03 => img03 will not be loaded.
            '''
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
        ''' returns the number of images in the list
        '''
        return self.imagecount

    
    def findItem(self, imToFind):
        ''' Searches through the list and finds the best match
        @param imToFind: the image to find in the list
        @return the entry number of the best match, None if no good matches are found
        '''
        maxval = 0
        maximg = 0
        #cv2.imshow("imtofind", imToFind)
        for i in range( 0, len(self.allImages)):
            result = cv2.matchTemplate(self.allImages[i], imToFind,cv2.TM_CCORR_NORMED)
            if len(result) == 0:
                continue
            
            curminval, curmaxval, curminloc, curmaxloc = cv2.minMaxLoc(result)  # @UnusedVariable
            if maxval < curmaxval:
                maxval = curmaxval
                maximg = i
 
            #cv2.imshow("im %f"%i, self.allImages[i])
        
        #cv2.waitKey()
            
    
        # TODO: magic val. threshold value for acceptance    
        if maxval < self._findThreshold:
            print >> sys.stderr, "maxval: %f"%maxval
            return None
    
        return maximg

    
    def getSize(self, entry): 
        '''
        @param entry: the entry to look up
        @return the width, height of the image
        '''
        shape = self.allImages[entry].shape
        return shape[1], shape[0]

        
    def setThreshold(self, threshold):
        ''' sets the threshold for acceptable match
        @param threshold a value between 0 and 1 
        (don't do 1.0 since the numeric stuff will make perfect matches 99.99%)

        '''
        self._findThreshold = threshold
        
        

    
    
    
    
    



