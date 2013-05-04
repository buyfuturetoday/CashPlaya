from data.point import point
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
        
        self._currentImage = None
        self._emptyImage = emptyImage
        self._value = '.'
                
    def isEmpty(self, image ):
        ''' compares the default empty image with the current picture '''
        self._currentImage = image[self.pointTopLeft.y:self.pointBottomRight.y+1,
                                  self.pointTopLeft.x:self.pointBottomRight.x+1, :]

        return numpy.array_equal(self._currentImage, self._emptyImage)



    
    
    

    
    

    
    

        