"""
file_operations Module:

This module provides functions for basic file operations like opening, writing, and closing files, as well as a function for introducing a wait time.

Functions:
    open_file(filename):
        Opens a file in write mode and returns a file object.
        
    write_to_file(file_obj, text):
        Writes 'text' to the file associated with 'file_obj'.
        
    close_file(file_obj):
        Closes the file associated with 'file_obj'.
        
    wait(seconds):
        Pauses the program's execution for 'seconds' seconds.
"""


import time

def open_file(filename):
    return open(filename, 'w')

def write_to_file(file_obj, text):
    print(text, file=file_obj)

def close_file(file_obj):
    file_obj.close()

def wait(seconds):
    time.sleep(seconds)





