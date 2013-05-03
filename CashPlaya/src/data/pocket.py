from data.point import point
import cv2
import sys
import numpy

class pocket( object ):
    ''' the square thing to hold an item '''
    size = 40 # measured and will never change :-)
    
    def __init__(self, offset, emptyImage ):
        ''' constructor
        @param offset: The  top-left corner of the pocket reltavie to 0,0 in the main image
        @param emptyImage: The image to be used to check if the pocket is empty
        ''' 
        self.PointTL = offset
        self.PointBR = offset+point(self.size-1, self.size-1 )
        
        self.currentImage = None
        self.emptyImage = emptyImage

                
    @property
    def pointTopLeft(self):
        return self.PointTL
    
    @property
    def pointBottomRight(self):
        return self.PointBR

    def isEmpty(self, image ):
        ''' compares the default empty image with the current picture '''
        self.currentImage = image[self.pointTopLeft.x:self.pointBottomRight.x,
                                  self.pointTopLeft.y:self.pointBottomRight.y,:]

        return numpy.array_equal(self.currentImage, self.emptyImage)

        