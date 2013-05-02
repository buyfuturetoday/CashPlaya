# taken from here:
# http://stackoverflow.com/questions/7597120/matchtemplate-in-opencv-with-python
#
# Some docs..
# - http://docs.opencv.org/doc/tutorials/imgproc/histograms/template_matching/template_matching.html
# - http://blog.matael.org/writing/a-first-try-at-ambilight/

import cv2
import glob
import sys

# templates
ScrewFilenameTopLeft = "Templates/TopLeftCornerScrew.png"
ScrewFilenameBotomRight = "Templates/BottomRightCornerScrew.png"

color_red = (0, 0, 255)

class point(object):
    ''' point class: basic x,y with add and subtract '''
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
    def __add__(self, otherpoint ):
        return point( self.x+otherpoint.x, self.y+otherpoint.y)
    
    def __sub__(self, otherpoint ):
        return point( self.x-otherpoint.x, self.y-otherpoint.y)
    
    @property
    def tupple(self):
        return self.x, self.y
    
class pocket( object ):
    ''' the square thing to hold an item '''
    def __init__(self, col, row, offset, size = 40 ):
        self.PointTL = offset+point(col*size, row*size )
        self.PointBR = offset+point((col+1)*size-1, (row+1)*size-1 )
        self.pos = point( col, row )
        self.offset = offset
        self.size = size
        
    @property
    def pointTopLeft(self):
        return self.PointTL
    
    @property
    def pointBottomRight(self):
        return self.PointBR

def FindCorner( image, screwtemplate, ShowTracking = True ):
    ''' using the template, the corner screw is found
    @return: the position of the corner screw
    '''
    w,h = screwtemplate.shape[:2]

    result = cv2.matchTemplate(screwtemplate,image,cv2.TM_CCORR_NORMED)
    
    minval, maxval, minloc, maxloc = cv2.minMaxLoc(result)  # @UnusedVariable
    
    if maxval < 1.0:
        print >> sys.stderr, "Note: match should be 100%%, was %f"%(maxval*100,)
    
    if ShowTracking:
        cv2.rectangle(image, maxloc, (maxloc[0]+w, maxloc[1]+h), color_red )
    
    return point(maxloc[0], maxloc[1])

def GenPockets( offset, ColCount = 7, RowCount = 7):
    ''' generates the pocket objects with default data '''
    pockets = []
    for col in range(0,ColCount):
        pockets.append([])
        for row in range(0,RowCount):
            pockets[col].append(pocket( col, row, offset ))

    return pockets
    
def CheckPocket( col, row):
    ''' checks if the '''
    pass

# load templates
screwtemplateTL = cv2.imread(ScrewFilenameTopLeft)
screwtemplateBR = cv2.imread(ScrewFilenameBotomRight)

for screenshotfilename in glob.glob("Screenshots/*.png"):
    image = cv2.imread( screenshotfilename )
    
    
    print "located corners in file %s"%screenshotfilename
    
    CornerTL = FindCorner( image, screwtemplateTL )
    print " - top-left: %d, %d"%CornerTL.tupple

    CornerBR = FindCorner( image, screwtemplateBR )
    print " - bottom-right: %d, %d"%CornerBR.tupple
    
    size = CornerBR -CornerTL
    print " - size: %d x %d"%size.tupple
    print ""

    # red rectangle around drop area
    # TODO: magic values!
    DropItemsAreaTL = CornerTL + point(15,95)
    DropItemsAreaBR = DropItemsAreaTL + point( 281, 80 )
    cv2.rectangle(image, DropItemsAreaTL.tupple, DropItemsAreaBR.tupple, color_red )

    # red squares in matrix
    offset = point( DropItemsAreaTL.x, DropItemsAreaBR.y )
    
    pockets = GenPockets( offset )

    # draw pockets
    for col in range(0,7):
        for row in range(0,7):
            cv2.rectangle(image, 
                          pockets[col][row].pointTopLeft.tupple,
                          pockets[col][row].pointBottomRight.tupple,
                          color_red )
            # TODO: add text here to show what the detected content is.
        
    # TODO: add rectangle aroung next items
    
    cv2.imshow(screenshotfilename, image)

    
# wait and cleanup
cv2.waitKey()
cv2.destroyAllWindows()
