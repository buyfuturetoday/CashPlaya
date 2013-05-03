from data.point import point
import sys
from data.pocket import pocket
import numpy

class pockets(object):
    pocketsize = 40 # measured and will never change :-)
    gridsize = point( 7 ,7 )
    
    currentImage = None

    def __init__(self, offset ):
        ''' constructor
        @param offset: The  top-left corner of the pocket reltavie to 0,0 in the main image
        @param emptyImage: The image to be used to check if the pocket is empty
        ''' 
        self.PointTL = offset
        self.PointBR = offset+7*point(self.pocketsize, self.pocketsize ) - point(1,1)

        self.initPockets()

 
    def initPockets(self):
        ''' generates the pocket objects with default data '''
        # TODO: replace with something sensible...
        smallBlackImage = numpy.zeros((self.pocketsize-1, self.pocketsize-1, 3), numpy.float32)
        
        self.pockets = {}
        self.emptyImageList = {}
        for col in range(0, self.gridsize.x):
            for row in range(0, self.gridsize.y):
                pointTL = self.PointTL + point( col*self.pocketsize, row*self.pocketsize)
                self.emptyImageList[(col, row)] = smallBlackImage
                self.pockets[(col, row)] = pocket( pointTL, self.emptyImageList[(col, row)] )
                
    @property
    def pointTopLeft(self):
        return self.PointTL
    
    @property
    def pointBottomRight(self):
        return self.PointBR
    
    def processImage(self, image):
        for col in range( 0, self.gridsize.x):
            for row in range( 0, self.gridsize.y):
                if self.pockets[(col, row)].isEmpty( image ):
                    #print >> sys.stderr, "[%d, %d] empty"%(col, row)
                    continue
        
        # TODO: do we have an issue with shallow vs. deep copy here?
        self.currentImage = image
        
        # True means success
        return True

    
    def isEmpty(self, col, row):
        return self.pockets[(col, row)].isEmpty( self.currentImage)

    
    def ShowPocketBoundaries(self, color, bigImage):
        for col in range( 0, self.gridsize.x):
            for row in range( 0, self.gridsize.y):
                self.pockets[(col, row)].ShowBoundary( color, bigImage )       
        
    
    
    
    
    
    
