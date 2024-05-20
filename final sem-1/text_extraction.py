'''
This module processes an image located at 'path', converts it to grayscale, 
extracts text from the image using the Tesseract OCR (Optical Character Recognition) engine, 
and writes the extracted text to a text file named 'fname.txt'.

Parameters:
    path (str): The file path to the input image.
    fname (str): The name for the output text file (without the extension).

Returns:
    str: The extracted text from the image.
'''

from PIL import Image, ImageOps
import tesseract_initialise
from image_processing import grey, open_img

def extract_text_from_image(path, fname):

    img = open_img(path)
    img = grey(img)

    text = tesseract_initialise.pytesseract.image_to_string(img)
    
    # Writing extracted text to a file
    with open(f"{fname}.txt", 'w') as file:
        file.write(text[:-1])

    return text[:-1]





