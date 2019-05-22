from tkinter import Tk
from tkinter.filedialog import asksaveasfile
from PIL import Image
import time
import os

def convert(filename,size,filetype):
    ####usage:
    #filename: the file path of the png, jpg or jpeg that is to be converted to an icon
    #size: can be (16,16),(32,32),(48,48),(64,64),(128,128),(256,256), 'Auto'
    #filetype: can be 'ico', 'icns', 'png'

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
                img=img.resize(size, Image.ANTIALIAS)
                img.save(filen)
                
            except:
                #'converts' the .ico file to .png so PIL can recognize it
                #after the file is generated and saved,
                #it becomes a .ico file

                os.remove(filen)

                a=filen.replace(".png",".ico")
                filen=filen.replace(".ico",".png")
                
                if size!='Auto':   
                    img=img.resize(size, Image.ANTIALIAS)

                img.save(filen)

                os.rename(filen,a)

        if filetype=='icns':
            if filen.lower().endswith(('icns'))==False:
                filen=filen+'.icns'
                
            try:
                img=img.resize(size, Image.ANTIALIAS)
                img.save(filen)

            except:  
                #'converts' the .icns file to .png so PIL can recognize it
                #after the file is generated and saved,
                #it becomes a .icns file
                
                a=filen.replace(".png",".icns")

                os.remove(filen)
                filen=filen.replace(".icns",".png")#converts file to png
                
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
    
