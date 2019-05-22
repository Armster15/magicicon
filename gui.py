from tkinter import Tk
import tkinter
from tkinter.filedialog import askopenfilename
from tkinter import ttk, StringVar
from PIL import Image, ImageTk
from tkinter import Canvas,W
from magicicon import *
import tkinter.messagebox
import os.path
import os


def validate(filetype):
    global w, filename
    value = size_var.get()


    if filename==None:
        tkinter.messagebox.showerror("File not selected","You have to select a file to convert!")
        
    elif filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        if value=='1':
            convert(filename,(16,16),filetype)

        elif value=='2':
            convert(filename,(32,32),filetype)

        elif value=='3':
            convert(filename,(48,48),filetype)
            
        elif value=='4':
            convert(filename,(64,64),filetype)

        elif value=='5':
            convert(filename,(128,128),filetype)

        elif value=='6':
            convert(filename,(256,256),filetype)

        elif value=='7':
            convert(filename,'Auto',filetype)

        else:
            tkinter.messagebox.showerror("Size not Selected","You have to select a size to convert the image into an icon.")

    else:
        extention = os.path.splitext(filename)[1]
        tkinter.messagebox.showerror("Unsupported file type", "File type {} not supported. \n \n File types supported are .jpeg, .jpg and.png".format(extention))
        
c=True
size=1
filename=None

def selectfile():
    global filename
    global changefiletext
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

    changefiletext.set(filename)
    
#Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
#filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
#print(filename)


radiobuttons = [
    ("16x16", "1"),
    ("32x32", "2"),
    ("48x48", "3"),
    ("64x64",'4'),
    ('128x128','5'),
    ('256x256','6'),
    ('Auto','7')
]


#if filename.lower().endswith(('.png', '.jpg', '.jpeg')):

root=Tk()

root.tk.call('wm', 'iconphoto', root._w, ImageTk.PhotoImage(file='images/icon.png')) #sets the icon of root

root.title('MagicIcon')
                
img = ImageTk.PhotoImage(Image.open('images/logo.png'))

m=tkinter.Label(root,image=img)
m.pack()

by=tkinter.Label(root,text="by Armaan Aggarwal \n ------------------------")
by.pack()


size_var = StringVar()
size_var.set('L')#initialize

changefiletext=StringVar()
changefiletext.set("Select a file")#initialize

filebutton = tkinter.Button(root, text ="Upload image", command=selectfile)

#dacanvas.create_text(100,10,text='hi', anchor=tkinter.W, fill='blue')


filebutton.pack(side=tkinter.TOP)

w = tkinter.Label(root,textvariable=changefiletext, text="Select a file")
w.pack()

f=tkinter.Label(root, text="------------------------")
f.pack()

##    R1 = tkinter.Radiobutton(root, text='16x16',variable=size_var, value = '1')
##    R2 = tkinter.Radiobutton(root, text='32x32',variable=size_var, value = '2')
##    R3 = tkinter.Radiobutton(root, text='48x48',variable=size_var, value = '3')
##    R4 = tkinter.Radiobutton(root, text='64x64',variable=size_var, value = '4')
##    R5 = tkinter.Radiobutton(root, text='128x128',variable=size_var, value = '5')
##    R6 = tkinter.Radiobutton(root, text='256x256',variable=size_var, value = '6')
##    R7 = tkinter.Radiobutton(root, text='Auto',variable=size_var, value = '7')

#radiolist=[R1,R2,R3,R4,R5,R6,R7]


for text, value1 in radiobuttons:
    b = tkinter.Radiobutton(root, text=text,
                    variable=size_var, value=value1)

    #print(size_var)

    b.pack(side=tkinter.TOP)


icobutton = tkinter.Button(root, text ="Convert to .ico!", command=lambda: validate('ico'))
icnsbutton = tkinter.Button(root, text ="Convert to .icns!", command=lambda: validate('icns'))
pngbutton = tkinter.Button(root, text ="Convert to .png!", command=lambda: validate('png'))

icobutton.pack(side=tkinter.TOP)
icnsbutton.pack(side=tkinter.TOP)
pngbutton.pack(side=tkinter.TOP)

##text=tkinter.Text(root)
##text.insert(tkinter.END, 'hi', 'color')
##text.pack()
##text['state']='disabled'






