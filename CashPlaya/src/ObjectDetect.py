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

def FindCorner( image, screwtemplate, ShowTracking = True ):
    w,h = screwtemplate.shape[:2]

    result = cv2.matchTemplate(screwtemplate,image,cv2.TM_CCORR_NORMED)
    
    minval, maxval, minloc, maxloc = cv2.minMaxLoc(result)  # @UnusedVariable
    
    if maxval < 1.0:
        print >> sys.stderr, "Note: match should be 100%%, was %f"%(maxval*100,)
    
    if ShowTracking:
        cv2.rectangle(image, maxloc, (maxloc[0]+w, maxloc[1]+h), ( 0, 0, 255 ) )
    
    return maxloc

# load templates
screwtemplateTL = cv2.imread(ScrewFilenameTopLeft)
screwtemplateBR = cv2.imread(ScrewFilenameBotomRight)

for screenshotfilename in glob.glob("Screenshots/*.png"):
    image = cv2.imread( screenshotfilename )
    
    
    print "located corners in file %s"%screenshotfilename
    
    CornerTL = FindCorner( image, screwtemplateTL )
    print " - top-left: %d, %d"%CornerTL

    CornerBR = FindCorner( image, screwtemplateBR )
    print " - bottom-right: %d, %d"%CornerBR
    
    print " - size: %d x %d"%(CornerBR[0]-CornerTL[0], CornerBR[1]-CornerTL[1])
    print ""

    cv2.imshow("image", image)


cv2.waitKey()

