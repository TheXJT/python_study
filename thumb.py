# -*- coding: utf-8 -*-
import os, sys
from PIL import Image
#convert image to thumb
for infile in sys.argv[1:]:
     outfile=os.path.splitext(infile)[0] + ".thumbnail"
     if infile !=outfile:
        try:
            im=Image.open(infile)
            x, y=im.size
            print(x,y)
            print(x/2,y/2)
            im.thumbnail((x//2,y//2))
            im.save(outfile,"JPEG")
        except IOError:
            print("cannot create thumbnail for ",infile)
