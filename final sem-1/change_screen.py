''' This module provides functions to switch between different screens in a graphical user interface (GUI) application.
    Functions:
    change_to_screen(old_frame,new_frame):
        Switches to the specified screen in the GUI application. '''

def change_to_screen(old_frame,new_frame):
        new_frame.pack(fill='both', expand=1)
        old_frame.pack_forget()


















