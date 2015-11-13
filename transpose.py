from PIL import Image

imageFName='test.jpg'

def image_transpose(image):
    '''
        Input: a Image instance
        Output: a trandposed Image instance
        Function:
            * switches the left and the right part of a Image instance
            * for the left part of the original instance, flips left and right and then make it upside doen.
    '''
    xsize, ysize=image.size
    xsizeLeft=xsize//2
    boxLeft=(0,0,xsizeLeft,ysize)
    boxRight=(xsizeLeft,0,xsize,ysize) 
    boxLeftNew=(0,0,xsize-xsizeLeft,ysize)
    boxRightNew=(xsize-xsizeLeft,0,xsize,ysize)
    partLeft=image.crop(boxLeft).transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_180)
    partRight=image.crop(boxRight)
    image.paste(partRight,boxLeftNew)
    image.paste(partLeft,boxRightNew)
    return image
if __name__=='__main__':
    avatar=Image.open(imageFName)
    avatar=image_transpose(avatar)
    avatar.show()
