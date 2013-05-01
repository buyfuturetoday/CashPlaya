# taken from here:
# http://stackoverflow.com/questions/7597120/matchtemplate-in-opencv-with-python
#
# Some docs..
# - http://docs.opencv.org/doc/tutorials/imgproc/histograms/template_matching/template_matching.html


from cv import *
import glob

# templates
ScrewFilenameTopLeft = "Templates/TopLeftCornerScrew.png"
ScrewFilenameBotomRight = "Templates/BottomRightCornerScrew.png"

def FindCorner( image, screwtemplate ):
    W,H = GetSize(image)
    w,h = GetSize(screwtemplate)
    
    width = W - w + 1
    height = H - h + 1
    
    result = CreateImage((width, height), 32, 1)
    MatchTemplate(image, screwtemplate, result, CV_TM_CCORR_NORMED)
    
    minval, maxval, minloc, maxloc = MinMaxLoc(result)
    
    if maxval < 1.0:
        print "Note: match should be 100%%, was %f"%(maxval*100,)
    
    ShowImage("Result", result)
    #WaitKey()
    
    return maxloc

# load templates
screwtemplateTL = LoadImage(ScrewFilenameTopLeft)
screwtemplateBR = LoadImage(ScrewFilenameBotomRight)

for screenshotfilename in glob.glob("Screenshots/*.png"):
    image = LoadImage( screenshotfilename )
    ShowImage("image", image)
    
    
    print "located corners in file %s"%screenshotfilename
    
    CornerTL = FindCorner( image, screwtemplateTL )
    print " - top-left: %d, %d"%CornerTL

    CornerBR = FindCorner( image, screwtemplateBR )
    print " - bottom-right: %d, %d"%CornerBR
    
    print " - size: %d x %d"%(CornerBR[0]-CornerTL[0], CornerBR[1]-CornerTL[1])
    print ""

WaitKey()

