import os

class ItemList(object):
        
    def __init__(self, itempath):
        self.path = itempath
        
        self.initImages( )
        pass
    
    def initImages(self):
        itemcounter = 0
        while True:
            filename = "%s/item_%02d.bmp"%(self.path, itemcounter)
            
            if not os.path.isfile( filename ):
                break

            itemcounter = itemcounter + 1
        
        self.imagecount = itemcounter+1

    @property
    def count(self):
        return self.imagecount
    
    
    
    



