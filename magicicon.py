import subprocess
import sys

def convert(filename,outputfile):
    import cloudconvert as c

    def get_extension(filename):
        import os.path
        return os.path.splitext(filename)[1]

    filen_extension=get_extension(filename)

    print("Uploading file to server...")

    api=c.Api('MJ9qM1Eu2PhM7yegfHBQiAjxrcUmGQCo3uC1yymNyPoiUGFhXIUpbtIHXkQjiBJP') #api key for cloudconvert 
    process = api.convert({
        'inputformat': filen_extension.replace('.',''),
        'outputformat': 'ico',
        'input': 'upload',
        'file': open(filename, 'rb')
    })
        
    print("Uploaded file to server. Converting....")
    process.wait()
    download_file_name=filename.replace(filen_extension,'.icns')
    print("Downloading....")
    process.download(outputfile)
    print("Done!")


