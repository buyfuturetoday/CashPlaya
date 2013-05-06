from data.BoardElement import BoardElement
from data.point import point
from data.Digit import Digit
import cv2
import sys

class ScoreBoard(BoardElement):
    _size = point(184, 39)
    _digit_rel_loc = [  point( 160, 5 ), 
                        point( 143, 5 ), 
                        point( 126, 5 ), 
                        point(  95, 5 ), 
                        point(  78, 5), 
                        point(  61, 5 ), 
                        point(  30, 5 ) ]
    _defaultDigitSize = point(20, 29 )
    
    def __init__(self, offset, digitlist ):
        ''' constructor
        ''' 
        super(ScoreBoard, self).__init__( offset, self._size)
        
        
        self._digitlist = digitlist
        
        # bogus boardelements - specific location is fixed later.
        self._digitelements = []
        for digit_loc in self._digit_rel_loc:
            self._digitelements.append( Digit(self.pointTopLeft+digit_loc, self._defaultDigitSize ))

    def ShowBoundary(self, color, overlayImage):
        super(ScoreBoard, self).ShowBoundary(color, overlayImage)
        for digit in self._digitelements:
            digit.ShowBoundary( color, overlayImage)
    
    def ReadScore(self, image ):
        digits = []
        widthadj = 0
        for i in range( 0, len( self._digit_rel_loc ) ):
            imToFind = self._digitelements[i].getImage( image )

            item = self._digitlist.findItem( imToFind )
            if item == None:
                # TODO: better handling of blanks.
#                 filename = 'digit_loc_%02d.png'%i
#                 cv2.imwrite( filename, imToFind )
#                 print >> sys.stderr, "digit not recognized: %s"%filename
                pass
            else:
                digits.append( item )

                res = self._digitlist.getLastResult()[item]

                size = point( *self._digitlist.getSize( item ) )
                widthadj = widthadj + res[3][0]

                self._digitelements[i] = Digit(self._digitelements[i].pointTopLeft+point(res[3][0], res[3][1]), 
                                               size )

                
            if i+1 < len( self._digit_rel_loc ):
                defaultDistance = 3 # dist between digits
                if (i+1) % 3 == 0:
                    ExtraOffset = point( 12+defaultDistance, 0 )
                else:
                    ExtraOffset = point( 0+defaultDistance, 0 )                    
                
                # recreate digit with better start point
                self._digitelements[i+1] = Digit(self._digitelements[i].pointTopLeft    \
                                                 - point( self._defaultDigitSize.x, 0) - ExtraOffset,
                                                 self._defaultDigitSize )

        # calculate the integer value
        digitssum = 0
        for i in range( 0, len(digits) ):
            digitssum = digitssum + digits[i]*10**i
        return digitssum
    
    
