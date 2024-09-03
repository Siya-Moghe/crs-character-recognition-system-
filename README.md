Semester 1 Python Mini Project
This is a character recognition system I've worked on for a class. It uses tesseract, PIL, tkinter, pygame and more.


Credits: All images were created on Canva


# Text from Image Project
## Overview
This project is a graphical user interface (GUI) application designed to extract text from images. It uses various Python libraries, including Tkinter for the GUI, PIL for image processing, and Pygame for sound. The application allows users to upload images, extract text, and save the extracted text to a file.

# Features
- Fullscreen Tkinter GUI
- Music playback using Pygame
- Image upload and text extraction
- Text extraction saved to a user-defined file

# Installation
- to run this project you will require Python and additional Python packages.
- make sure you have the packages: [pillow](https://pillow.readthedocs.io/en/stable/), [pygame](https://www.pygame.org/download.shtml), [pytesseract](https://pypi.org/project/pytesseract/)
- setup Tesseract OCR: download and install tesseract ocr, after which you will need to update the path in "tesseract_initialise.py" within the path_to_tesseract variable.

 # How To Run
  - start the application by running main_program.py
  - The first screen to show up will be "start screen" : click the let's begin! button to move to the file selection screen.
  - File Selection Screen: submit a file name, this file will be opened for writing any extracted text. Next the uplad image screen will open up.
  - Upload Image : Upload an image from where text is to be read, click extract text.
  - finally click the exit button to leave the application

 # Modules

    ### main_program.py
    This is the main script of the application. It sets up the GUI using Tkinter, handles the user interactions and manages the different operations.

    ### change_screen.py
    It provides functions to switch between different screens in GUI.

    ### file_operations.py
    Handles all the basic file operations such as opening, writing, closing files and also introduces a wait time.

    ### image_processing.py
    Conatins the functions used for image processing with PIL including converting images to grayscale.

    ### tesseract_initialise.py
    This simply configures tesseract ocr using the pytesseract library.
    
