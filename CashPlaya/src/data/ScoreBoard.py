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
                filename = 'digit_loc_%02d.png'%i
                cv2.imwrite( filename, imToFind )
                print >> sys.stderr, "digit not recognized: %s"%filename
            else:
                digits.append( item )

                res = self._digitlist.getLastResult()[item]
                print "item: %d, result: %f, pos %s"%(item, res[1], res[3])

                size = point( *self._digitlist.getSize( item ) )
#                widthadj = widthadj + self._defaultDigitSize.x - size.x
                widthadj = widthadj + res[3][0]

                # update current element with new size
                # size is known by detected item.
                # TopLeft is oldBottomRight-size+p(1,1) - where it was detected
#                 self._digitelements[i] = Digit(self._digitelements[i].pointBottomRight-size+point(1,1)-point(res[3][0], res[3][1]), 
#                                                size )
                self._digitelements[i] = Digit(self._digitelements[i].pointTopLeft+point(res[3][0], res[3][1]), 
                                               size )

                print "digit %d width: %d (acc: %d)"%(item, size.x, widthadj)
#                 print self._digitelements[i].pointTopLeft
#                 print self._digitelements[i].pointBottomRight
#                                 
#                 print self._digitelements[i].pointBottomRight   \
#                                                  - point( self._defaultDigitSize.x, 0 )

                
            if i+1 < len( self._digit_rel_loc ):
                
                if (i+1) % 3 == 0:
                    ExtraOffset = point( 12+3, 0 )
                else:
                    ExtraOffset = point( 0+3, 0 )                    
                
                # recreate digit with better start point
                self._digitelements[i+1] = Digit(self._digitelements[i].pointTopLeft    \
                                                 - point( self._defaultDigitSize.x, 0) - ExtraOffset,
                                                 self._defaultDigitSize )

#             cv2.imshow("imtofind", imToFind)
#             cv2.waitKey()
        
        for digit in self._digitelements:
            print digit.pointTopLeft
        print digits
        digitssum = 0
        for i in range( 0, len(digits) ):
            digitssum = digitssum + digits[i]*10**i
        return digitssum
    
    
