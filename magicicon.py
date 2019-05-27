from tkinter import Tk
from tkinter.filedialog import asksaveasfile
from PIL import Image
import time
import os
from utils import randomstring #to ensure that files won't be corrupted during conversion

def convert(filename,size,filetype):
    """Converts a .png, .jpeg or .jpg into a .ico, .icns or .png icon file
    Usage ↓
    filename: the file path of the png, jpg or jpeg that is to be converted to an icon.
    size: can be (16,16),(32,32),(48,48),(64,64),(128,128),(256,256), 'Auto'.
    filetype: can be 'ico', 'icns', 'png'. """

    string=randomstring(12)#to ensure that files wont get corrupted during conversion
    string=string+'.png.png'
    
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        if filetype=='ico':
            filet = [('.ico (Windows Icon File)', '*.ico')]

        if filetype=='icns':
            filet = [('.icns (Apple Icon File)', '*.icns')]

        if filetype=='png':
            filet = [('.png File', '*.png')]

        Tk().withdraw()
        
        try:
            filen = asksaveasfile(filetypes=filet).name
            
        except:
            return
        
        img=Image.open(filename)
        
        if filetype=='ico':
            if filen.lower().endswith(('ico'))==False:
                filen=filen+'.ico'
            
            try:
                if size=='Auto':
                
                    img.save(filen)

                else:
                    img=img.resize(size, Image.ANTIALIAS)
                    
            except:
                #'converts' the .ico file to .png so PIL can recognize it
                #after the file is generated and saved,
                #it becomes a .ico file
                os.remove(filen)

                a=filen.replace(string,".ico")
                filen=filen.replace(".ico",string)
                
                if size!='Auto':   
                    img=img.resize(size, Image.ANTIALIAS)

                img.save(filen)

                os.rename(filen,a)

        if filetype=='icns':
            if filen.lower().endswith(('icns'))==False:
                filen=filen+'.icns'
                
            try:
                if size=='Auto':
                
                    img.save(filen)

                else:
                    img=img.resize(size, Image.ANTIALIAS)

            except:  
                #'converts' the .icns file to .png so PIL can recognize it
                #after the file is generated and saved,
                #it becomes a .icns file
                
                a=filen.replace(string,".icns")

                os.remove(filen)
                filen=filen.replace(".icns",string)#converts file to png
                
                if size!='Auto':   
                    img=img.resize(size, Image.ANTIALIAS)
                
                img.save(filen)

                time.sleep(.5)

                os.rename(filen,a)#converts back to .icns

            if filetype=='png':
                if filen.lower().endswith(('png'))==False:
                    filen=filen+'.png'

                img=img.resize(size, Image.ANTIALIAS)
                img.save(filen)






    else:
        raise FileExistsError("Unsupported file type", "File type not supported. File types supported are .jpeg, .jpg and.png")
    
