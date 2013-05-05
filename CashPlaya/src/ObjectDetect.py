# taken from here:
# http://stackoverflow.com/questions/7597120/matchtemplate-in-opencv-with-python
#
# Some docs..
# - http://docs.opencv.org/doc/tutorials/imgproc/histograms/template_matching/template_matching.html
# - http://blog.matael.org/writing/a-first-try-at-ambilight/
# - http://stackoverflow.com/questions/7670112/finding-a-subimage-inside-a-numpy-image


import cv2
import glob
import sys
import numpy
from data.point import point
from data.pocket import pocket
from data.pockets import pockets
from data.ItemList import ItemList
from data.ScoreBoard import ScoreBoard

# templates
ScrewFilenameTopLeft = "Templates/TopLeftCornerScrew.png"
ScrewFilenameBotomRight = "Templates/BottomRightCornerScrew.png"

color_red = (0, 0, 255)
      
emptyImageList = {}
for col in range( 0, 7):
    for row in range( 0, 7):
        fname = "Templates/004_c%d_r%d.bmp"%(col, row)
        emptyImageList[(col, row)] = cv2.imread(fname)
        
items = ItemList( 'Templates' )
digits = ItemList( 'Templates', 'digit_%d.bmp')

def FindCorner( image, screwtemplate, ShowTracking = False ):
    ''' using the template, the corner screw is found
    @return: the position of the corner screw
    '''
    result = cv2.matchTemplate(screwtemplate,image,cv2.TM_CCORR_NORMED)
    minval, maxval, minloc, maxloc = cv2.minMaxLoc(result)  # @UnusedVariable

    if maxval < 1.0:
        print >> sys.stderr, "Note: match should be 100%%, was %f"%(maxval*100,)
    
    if ShowTracking:
        w,h = screwtemplate.shape[:2]
        cv2.rectangle(image, maxloc, (maxloc[0]+w, maxloc[1]+h), color_red )
    
    return point(maxloc[0], maxloc[1])


# load templates
screwtemplateTL = cv2.imread(ScrewFilenameTopLeft)
screwtemplateBR = cv2.imread(ScrewFilenameBotomRight)
fileno = 0

for screenshotfilename in glob.glob("Screenshots/*.png"):
#for screenshotfilename in glob.glob("Screenshots/Screenshot - 2013-05-01 - 21:35:24.png"):

    image = cv2.imread( screenshotfilename )
    
    
    print "located corners in file %s"%screenshotfilename
    
    CornerTL = FindCorner( image, screwtemplateTL )
    print " - top-left: %d, %d"%CornerTL.tupple

    CornerBR = FindCorner( image, screwtemplateBR )
    print " - bottom-right: %d, %d"%CornerBR.tupple
    
    size = CornerBR -CornerTL
    print " - size: %d x %d"%size.tupple
    print ""

    # TODO: magic values!
    DropItemsAreaTL = CornerTL + point(15,95)
    DropItemsAreaBR = DropItemsAreaTL + point( 281, 80 )

    ScoreBoardOffset = point( 71, 34 ) # scoreboard relative to screw
    curScoreBoard = ScoreBoard( CornerTL + ScoreBoardOffset, digits)

    # red squares in matrix
    offset = point( DropItemsAreaTL.x, DropItemsAreaBR.y )

    curPockets = pockets( offset, emptyImageList )
    curPockets.processImage(image)
    
    fileno = fileno + 1
    emptycount = 0
    unknownCount = 0

    # draw pockets 
    for col in range(0,7):
        for row in range(0,7):
            if curPockets.isEmpty(col, row):
                emptycount += 1
                curPockets.setValue(col, row, 'X')
                continue
            
            item = items.findItem( curPockets.getImage(col, row))
            if item is None:
                filename = "imgstore/%03d_c%d_r%d.bmp"%(fileno, col, row)
                #print "[%d, %d] not empty and not detected saving to %s"%(col, row, filename)                
                cv2.imwrite( filename, curPockets.getImage(col, row) )
                unknownCount = unknownCount + 1
            else:
                #print "[%d, %d] detected as %02d"%(col, row, item, )                
                curPockets.setValue(col, row, str(item))
                pass


    # add the tracking rectangles and other stuff
    curScoreBoard.ShowBoundary( (255, 255, 0), image)
    curPockets.ShowPocketBoundaries( (0,0,255), image)
    curPockets.ShowPocketValues( (0,0, 255), image)

    cv2.imshow("%d: %s"%(fileno, screenshotfilename), image)
    cv2.imwrite("imgstore/%03d.png"%fileno, image)
    cv2.imwrite("imgstore/%03d_score.png"%fileno, curScoreBoard.getImage(image))    
    print "file %d"%fileno
    print "- emptycount %d"%emptycount
    print "- unknowncount %d"%unknownCount
    print ""
    
# wait and cleanup
cv2.waitKey()
cv2.destroyAllWindows()
