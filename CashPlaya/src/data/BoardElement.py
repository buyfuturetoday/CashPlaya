from data.point import point

class BoardElement(object):
    def __init__(self, offset, size ):
        ''' constructor
        @param offset: The  top-left corner of the pocket reltavie to 0,0 in the main image
        @param emptyImage: The image to be used to check if the pocket is empty
        ''' 
        self._PointTL = offset
        self._PointBR = offset+size - point(1,1)
    
    @property
    def pointTopLeft(self):
        return self._PointTL
    
    @property
    def pointBottomRight(self):
        return self._PointBR    
    
    pass


