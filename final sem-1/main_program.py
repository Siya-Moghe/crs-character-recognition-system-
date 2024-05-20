
from tkinter import *
from tkinter import filedialog, font
from PIL import ImageTk, Image
import file_operations
import text_extraction
import change_screen as cs
import time
from image_processing import open_img,grey
from pygame import mixer  

#sets music using mixer

mixer.init()
mixer.music.load('sound.mp3')
mixer.music.play()

# creating mainscreem root
root = Tk()
root.title('text from image project')
root.attributes('-fullscreen', True)
root.configure(bg='black')

Checkbutton1 = IntVar() 

# creating file_frame

file_frame = Frame(root)
bgimg_file_frame= PhotoImage(file = r"file_screen.png")
limg_file= Label(file_frame, i=bgimg_file_frame).place(relx=0.5,rely=0.5,anchor="center")


# creating start_frame

bgimg_start_frame= PhotoImage(file = r"start_frame_bg.png")
start_frame = Frame(root,width = 800, height = 400)
start_frame.pack(padx=0,pady=50)

limg= Label(start_frame, i=bgimg_start_frame).place(relx=0.5,rely=0.5,anchor="center")


myFont = font.Font(size=30, family='Helvetica')

# making let's begin button

buttonswitch_1 = Button(start_frame,height=10, width=50, text="Let's Begin!",
                        bg="#E0E0E0", activebackground='#FFCCE5',
                        command= lambda :cs.change_to_screen(start_frame,file_frame))

buttonswitch_1['font'] = myFont

buttonswitch_1.pack(padx=400,pady=300)




fname = ''
f = ''

#file_entry takes the input to name the file where extracted text is to be printed

def file_entry():
    global x, e1, fname
    fname = StringVar()
    myFont = font.Font(size=30, family='Helvetica')
    if Checkbutton1.get() == 1:
        x = Label(file_frame, text='enter file name',font=myFont, bg='#CBB6AC', fg='black').pack()
        e1 = Entry(file_frame, textvariable=fname, bg='#E4DCD0', fg='black').pack(padx=20,pady=10)
        bs = Button(file_frame, text="submit", font=myFont, command=submit, bg='#3B5060', fg='white').pack()


# submit button and opening the file

def submit():
    global fn, f
    fn = e1
    myFont = font.Font(size=30, family='Helvetica')
    f = file_operations.open_file(str(fname.get()) + '.txt')
    file_operations.wait(0.5)
    y = Label(file_frame, text="file opened", font=myFont, bg='#CBB6AC', fg='black' ).pack(padx=20,pady=10)
    file_operations.wait(0.5)
    buttonswitch = Button(file_frame, text="next step", font=myFont, bg='#3B5060', fg='white', command= lambda :cs.change_to_screen(file_frame,print_frame)).pack()



myFont2 = font.Font(size=30, family='Helvetica')

bf = Checkbutton(file_frame, text="Start", font = myFont, activeforeground='black',foreground = "black", background = "#E4DCD0", 
                 activebackground='#EAD3CA', command=file_entry, variable=Checkbutton1,
                 onvalue=1, offvalue=0, height=2, width=10)

bf.pack(padx=100,pady=10)

# creating the print_frame

print_frame = Frame(root)
bgimg_print_frame= PhotoImage(file = r"file_screen.png")
limg_print= Label(print_frame, i=bgimg_print_frame).place(relx=0.5,rely=0.5,anchor="center")

newline = Label(print_frame)
uploaded_img = Label(print_frame)


def extract_and_display_text(path):
    extracted_text = text_extraction.extract_text_from_image(path, fname.get())
    Label(print_frame, text=extracted_text, font=('Times', 15, 'bold')).pack()
    time.sleep(0.5)
    exit_button = Button(root, text="Exit", command=root.quit).pack(pady=20) 
    


def show_extract_button(path):
    extractBtn = Button(print_frame, text="Extract text",
                        command=lambda: extract_and_display_text(path),
                        bg="#243440", fg="white", pady=25, padx=15, font=('Times', 25, 'italic'))
    extractBtn.pack()


def upload():
    try:
        path = filedialog.askopenfilename()
        image = open_img(path)
        img = ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image = img
        show_extract_button(path)
    except:
        pass


uploadbtn = Button(print_frame, text="Upload an image", command=upload,
                   bg="#243440", fg="white", height=2, width=20, pady=30, font=('Times', 25, 'italic')).pack()
newline.configure(text='\n')
newline.pack()
uploaded_img.pack()

root.mainloop()
