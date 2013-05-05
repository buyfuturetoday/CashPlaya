from data.BoardElement import BoardElement
from data.point import point
from data.Digit import Digit

class ScoreBoard(BoardElement):
    _size = point(184, 39)
    _digit_rel_loc = [  point( 160, 4 ), 
                        point( 143, 4 ), 
                        point( 126, 4 ), 
                        point(  96, 4 ), 
                        point(  79, 4), 
                        point(  62, 4 ), 
                        point(  32, 4 ) ]
    
    def __init__(self, offset, digitlist ):
        ''' constructor
        ''' 
        super(ScoreBoard, self).__init__( offset, self._size)
        defaultDigitSize = point(15, 30 )
        
        self._digitlist = digitlist
        
        self._digitelements = []
        for digit_loc in self._digit_rel_loc:
            self._digitelements.append( Digit(self.pointTopLeft+digit_loc, defaultDigitSize ))
        
#     def readScore(self, image):
#         for location in digit_location:
#             digit_img = 

    def ShowBoundary(self, color, overlayImage):
        super(ScoreBoard, self).ShowBoundary(color, overlayImage)
        for digit in self._digitelements:
            digit.ShowBoundary( color, overlayImage)