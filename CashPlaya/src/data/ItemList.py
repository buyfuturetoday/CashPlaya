# links:
# - http://stackoverflow.com/questions/7589012/combining-two-images-with-opencv

import os
import cv2
import numpy

class ItemList(object):
        
    def __init__(self, itempath):
        self.path = itempath
        
        self.initImages( )
        pass
    
    def initImages(self):
        itemcounter = 0
        images = []
        height = 0
        width = 0
        
        # loop until no more files
        while True:
            filename = "%s/item_%02d.bmp"%(self.path, itemcounter)

            if not os.path.isfile( filename ):
                break

            images.append( cv2.imread( filename ) )

#             height = height + images[-1].shape[0]            
#             if images[-1].shape[0] > width:
#                 width = images[-1].shape[0]
            itemcounter = itemcounter + 1
            
        # and save the result        
        self.imagecount = itemcounter
        self.itemsize = width
#         self.allImages = numpy.zeros((height, width, 3), numpy.uint8)
        self.allImages = images
                
#         h, w = images[0].shape[:2]
#         for i in range(0, self.imagecount):
#             self.allImages[i*h:(i+1)*h, :w ] = images[i]
        

    @property
    def count(self):
        return self.imagecount

    
    def findItem(self, imToFind):
#         result = cv2.matchTemplate(self.allImages, imToFind,cv2.TM_CCORR_NORMED)
#         minval, maxval, minloc, maxloc = cv2.minMaxLoc(result)  # @UnusedVariable
# 
# #         # TODO: magic value...
# #         if maxval < 0.8:
# #             return None
#         print maxloc
#         print maxval
# 
#         # make a drawing, it will explain it.
#         return round(maxloc[1]/float(self.itemsize) + 0.49)

        maxval = 0
        maximg = 0
        for i in range( 0, len(self.allImages)):
            #print i
            result = cv2.matchTemplate(self.allImages[i], imToFind,cv2.TM_CCORR_NORMED)
            #print result
            if maxval < result[0]:
                maxval = result[0]
                maximg = i
    
        # TODO: magic val. threshold value for acceptance    
        if maxval < 0.99:
            return None
    
        return maximg
    
    
    



