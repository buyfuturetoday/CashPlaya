from data.point import point
from data.BoardElement import BoardElement

class Digit( BoardElement ):
    _elementsize = point( 7, 30 )
    
    def __init__(self, offset ):
        super(Digit, self).__init__( offset, self._elementsize )


