from data.BoardElement import BoardElement
from data.point import point
from data.Digit import Digit

class ScoreBoard(BoardElement):
    _size = point(184, 39)
    _digit_rel_loc = [  point( 170, 3 ), 
                        point( 140, 3 ), 
                        point( 110, 3 ), 
                        point( 90, 3 ), 
                        point( 65, 3 ), 
                        point( 40, 3 ), 
                        point( 25, 3 ), 
                        point( 13, 3 ) ]
    
    def __init__(self, offset, digitlist ):
        ''' constructor
        ''' 
        super(ScoreBoard, self).__init__( offset, self._size)
        
        self._digitlist = digitlist
        
        self._digitelements = []
        for digit_loc in self._digit_rel_loc:
            self._digitelements.append( Digit(self.pointTopLeft+digit_loc ))
        
#     def readScore(self, image):
#         for location in digit_location:
#             digit_img = 

    def ShowBoundary(self, color, overlayImage):
        for digit in self._digitelements:
            digit.ShowBoundary(self, color, overlayImage)