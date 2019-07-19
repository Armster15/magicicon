from __future__ import print_function
    
import subprocess
import sys

def convert(filename,outputfile):
    import cloudconvert as c

    # to write output to output.txt
    o=open('output.txt', 'w')

    def get_extension(filename):
        import os.path
        return os.path.splitext(filename)[1]

    filen_extension=get_extension(filename)

    print('Uploading file to server...',file=o)

    api=c.Api('MJ9qM1Eu2PhM7yegfHBQiAjxrcUmGQCo3uC1yymNyPoiUGFhXIUpbtIHXkQjiBJP') #api key for cloudconvert 
    process = api.convert({
        'inputformat': filen_extension.replace('.',''),
        'outputformat': 'ico',
        'input': 'upload',
        'file': open(filename, 'rb')
    })
        
    print('Uploaded file to server. Converting....',file=o)

    process.wait()

    download_file_name=filename.replace(filen_extension,'.icns')

    print('Downloading....',file=o)
    process.download(outputfile)

    print('Done!',file=o)


