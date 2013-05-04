from data.point import point
import cv2
import sys
import numpy
from data.BoardElement import BoardElement

class pocket( BoardElement ):
    ''' the square thing to hold an item '''
    size = 40 # measured and will never change :-)
    
    def __init__(self, offset, emptyImage ):
        ''' constructor
        @param offset: The  top-left corner of the pocket reltavie to 0,0 in the main image
        @param _emptyImage: The image to be used to check if the pocket is empty
        ''' 
        super(pocket, self).__init__( offset, point(self.size, self.size) )
        
#         self._PointTL = offset
#         self._PointBR = offset+point(self.size-1, self.size-1 )
        
        self._currentImage = None
        self._emptyImage = emptyImage
        self._value = '.'
                
#     @property
#     def pointTopLeft(self):
#         return self._PointTL
#     
#     @property
#     def pointBottomRight(self):
#         return self._PointBR

    def isEmpty(self, image ):
        ''' compares the default empty image with the current picture '''
        self._currentImage = image[self.pointTopLeft.y:self.pointBottomRight.y+1,
                                  self.pointTopLeft.x:self.pointBottomRight.x+1, :]

        return numpy.array_equal(self._currentImage, self._emptyImage)

    
#     def ShowBoundary(self, color, overlayImage):
#         ''' draw a rectangle around the location of the pocket '''
#         cv2.rectangle(overlayImage, 
#                       self.pointTopLeft.tupple,
#                       self.pointBottomRight.tupple,
#                       color )

    
#     def getImage(self, image):
#         return image[ self.pointTopLeft.y:self.pointBottomRight.y, self.pointTopLeft.x:self.pointBottomRight.x]

    
#     def setValue(self, value):
#         self._value = value
# 
#     @property
#     def value(self):
#         return self._value
# 
#     
#     def ShowValue(self, color, overlayImage):
#         org = (self._PointTL + point( 3, 13)).tupple
#         cv2.putText(overlayImage, self.value, org,
#             cv2.FONT_HERSHEY_PLAIN, 1.0, color, thickness=2 )

    
    
    

    
    

    
    

        