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
    

def FindCorner( image, screwtemplate, ShowTracking = True ):
    w,h = screwtemplate.shape[:2]

    result = cv2.matchTemplate(screwtemplate,image,cv2.TM_CCORR_NORMED)
    
    minval, maxval, minloc, maxloc = cv2.minMaxLoc(result)  # @UnusedVariable
    
    if maxval < 1.0:
        print >> sys.stderr, "Note: match should be 100%%, was %f"%(maxval*100,)
    
    if ShowTracking:
        cv2.rectangle(image, maxloc, (maxloc[0]+w, maxloc[1]+h), color_red )
    
    return point(maxloc[0], maxloc[1])

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
    # TODO: magic values!
    size = 40   # square areas
    for col in range(0,7):
        for row in range(0,7):
            cv2.rectangle(image, 
                          (offset+point(col*size, row*size )).tupple, 
                          (offset+point((col+1)*size, (row+1)*size )).tupple, 
                          color_red )

        
    # TODO: add rectangle aroung next items
    
    cv2.imshow("image", image)

    
# wait and cleanup
cv2.waitKey()
cv2.destroyAllWindows()
