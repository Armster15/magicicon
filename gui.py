import sys
import tkinter
import tkinter.messagebox

if sys.platform=='win32':
    import errorwindow

from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfile
from tkinter import ttk, StringVar
from PIL import Image, ImageTk
from tkinter import Canvas,W
from magicicon import convert
import os.path
import os
from sys import exit
from tkinter import ttk
import webbrowser



import glob, os

output='None'

if sys.platform=='win32' or sys.platform=='darwin':
    path=(os.path.dirname(sys.argv[0]))
else:
    path=os.path.realpath(__file__)

# print(os.listdir(os.curdir))

c=True
size=1
filename=None
filet=None

def info():
    tkinter.messagebox.showinfo('About MagicIcon',' Version 2.0.0 \n \
Created by Armaan Aggarwal \n on July 15, 2019')

def view_on_github():
    webbrowser.open_new_tab(
        'https://github.com/armaan115/magicicon')

def reporterror_func():
    webbrowser.open_new_tab(
        'https://github.com/armaan115/magicicon/issues/new')

def on_close():
    global errorwindow
    root.destroy()
    del errorwindow

def error(errortitle, message):
    #For now, it will only pop up an error, not print.
    #print()
    #print("ERROR: {0}: {1}".format(errortitle,message)) #for output window

        
    tkinter.messagebox.showerror(errortitle,message)#for messagebox

def is_connected():
    import socket
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("www.github.com", 80))
        return True
    except OSError:
        pass
    return False

def selectfile():
    global filename
    global changefiletext
    global _2f

    _2f.configure(text="No output produced",foreground="black")
    _2f.update()

    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

    a=filename.replace(' ',"")#for checking if file is selected or not
    if a!='':
        changefiletext.set(filename)
    else:
        filename=None

def saveas(filetype):
    global filename
    global filet
    global _2f

    from cloudconvert.exceptions import(
    APIError, HTTPError, BadRequest, ConversionFailed, TemporaryUnavailable, InvalidResponse, InvalidParameterException
    )#we need this just in case if the user puts in a bad file (pdf to ico is one example)

    _2f.configure(text="No output produced",foreground="black")
    _2f.update()

    if filename!=None:
        if filetype=='.ico':
            filet = [('.ico (Windows Icon File)', '*.ico')]

        if filetype=='.icns':
            filet = [('.icns (Apple Icon File)', '*.icns')]

        if filetype=='.png':
                filet = [('.png File', '*.png')]
                
        filen = asksaveasfile(mode='w', defaultextension=filetype,filetypes=filet)
        if filen=='' or filen is None:
            return
        else:
            filen=filen.name
            _2f.configure(text='Converting...',foreground="black")
            _2f.update()
            os.remove(filen)#to prevent user confusion
        try:
            convert(filename,filen)
            _2f.configure(text='Completed!')
            _2f.update()
            
        except BadRequest:
            _2f.configure(text='ERROR: Invalid Input file',foreground="red")

            error("Invalid Input file","Unable to convert the requested file into an \
icon file. Either the file is corrupted or the inputed file simply cannot be converted into an icon file.")

        except HTTPError:
            _2f.configure(text='ERROR: Cannot connect to server',foreground="red")

            error("Cannot connect to server", "Cannot connect to server. Try looking \
at your internet connection and restart the program.")

    else:
        tkinter.messagebox.showerror('No file selected','You have to select a file to create an icon file!')#for messagebox
    
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

iconpath=os.path.normpath(r'{}/media/icon.png'.format(path))   
imgicon=Image.open('media/icon.png')
root.tk.call('wm', 'iconphoto', root._w, 
    ImageTk.PhotoImage(imgicon)) #sets the icon of root

root.title('MagicIcon')

root.protocol("WM_DELETE_WINDOW",  on_close)

titleimg=os.path.normpath('{}\media\logo.png'.format(path))        
img = ImageTk.PhotoImage(Image.open('media/logo.png'))
m=tkinter.Label(root,image=img)
m.pack()

# e = tkinter.Button(root, text="About", command=info)
# e.pack()

# by=tkinter.Label(root,text=" v2.0.0 created by  \n Armaan Aggarwal \n on July 15, 2019 \n ------------------------")
# by.pack()

size_var = StringVar()
size_var.set('L')#initialize

changefiletext=StringVar()
changefiletext.set("Select a file")#initialize

filebutton = tkinter.Button(root, text ="Upload image", command=selectfile)

#dacanvas.create_text(100,10,text='hi', anchor=tkinter.W, fill='blue')


filebutton.pack(side=tkinter.TOP)

w = tkinter.Label(root,textvariable=changefiletext, text="Select a file")
w.pack()

f=tkinter.Label(root, text="------------------------ \n Output:")
f.pack()

_2f=tkinter.Label(root, text="No output produced.")
_2f.pack()

_3f=tkinter.Label(root, text="------------------------")
_3f.pack()

##    R1 = tkinter.Radiobutton(root, text='16x16',variable=size_var, value = '1')
##    R2 = tkinter.Radiobutton(root, text='32x32',variable=size_var, value = '2')
##    R3 = tkinter.Radiobutton(root, text='48x48',variable=size_var, value = '3')
##    R4 = tkinter.Radiobutton(root, text='64x64',variable=size_var, value = '4')
##    R5 = tkinter.Radiobutton(root, text='128x128',variable=size_var, value = '5')
##    R6 = tkinter.Radiobutton(root, text='256x256',variable=size_var, value = '6')
##    R7 = tkinter.Radiobutton(root, text='Auto',variable=size_var, value = '7')

#radiolist=[R1,R2,R3,R4,R5,R6,R7]


##for text, value1 in radiobuttons:
##    b = tkinter.Radiobutton(root, text=text,
##                    variable=size_var, value=value1)
##
##    #print(size_var)
##
##    b.pack(side=tkinter.TOP)


icobutton = tkinter.Button(root, text ="Convert to .ico!", command=lambda: saveas('.ico'))
icnsbutton = tkinter.Button(root, text ="Convert to .icns!", command=lambda: saveas('.icns'))
pngbutton = tkinter.Button(root, text ="Convert to .png!", command=lambda: saveas('.png'))

icobutton.pack(side=tkinter.TOP)
icnsbutton.pack(side=tkinter.TOP)
pngbutton.pack(side=tkinter.TOP)

z=tkinter.Label(root, text=" ")
z.pack()

reporterror=os.path.normpath(r'{}\media\report_error.png'.format(path))        
img2 = ImageTk.PhotoImage(Image.open('media/report_error.png'))
r = tkinter.Button(root, text="Report an Error", image=img2, highlightthickness = 0, bd = 0, command=reporterror_func)
r.pack()


aboutimg=os.path.normpath(r'{}\media\About2.png'.format(path))        
infoimg = ImageTk.PhotoImage(Image.open('media/About2.png'))
infopack = tkinter.Button(root, text="About", image=infoimg, highlightthickness = 0, bd = 0, command=info)
infopack.pack()

viewongit=os.path.normpath(r'{}\media\ViewOnGithub.png'.format(path))        
gitimg = ImageTk.PhotoImage(Image.open('media/ViewOnGithub.png'))
gitpack = tkinter.Button(root, text="View on Github", image=gitimg, highlightthickness = 0, bd = 0, command=view_on_github)
gitpack.pack()

# if is_connected()==False:
#     tkinter.messagebox.showerror("No internet connection", "An internet connection is required \
# for this program to function. Please connect to the Internet and restart this tool.")
#     root.destroy()
#     exit()

root.mainloop()


