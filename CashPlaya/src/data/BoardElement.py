from data.point import point
import cv2

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
    
    def ShowBoundary(self, color, overlayImage):
        ''' draw a rectangle around the location of the pocket '''
        cv2.rectangle(overlayImage, 
                      self.pointTopLeft.tupple,
                      self.pointBottomRight.tupple,
                      color )

    def setValue(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

    
    def ShowValue(self, color, overlayImage):
        org = (self._PointTL + point( 3, 13)).tupple
        cv2.putText(overlayImage, self.value, org,
            cv2.FONT_HERSHEY_PLAIN, 1.0, color, thickness=2 )
    
    def getImage(self, image):
        return image[ self.pointTopLeft.y:self.pointBottomRight.y+1, self.pointTopLeft.x:self.pointBottomRight.x+1]
    
    
