''' 
This module provides functions for image processing using the PIL (Python Imaging Library) library.

Functions:
    grey(pic):
        Converts the input image 'pic' to grayscale using PIL's ImageOps module and returns the modified image.
        
    open_img(path):
        Opens an image file located at 'path' using PIL's Image module and returns the image object.
 '''
 

from PIL import Image, ImageOps

def grey(pic):
    pic = ImageOps.grayscale(pic)
    return pic

def open_img(path):
    pic = Image.open(path)
    return pic















