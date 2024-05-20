'''
This module provides functionalities to configure the Tesseract OCR settings
using the pytesseract library in Python. It allows users to set the path to the
Tesseract executable to enable OCR functionality.
'''

import pytesseract 

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = path_to_tesseract

