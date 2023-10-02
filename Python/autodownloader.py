import os
import requests
from sys import *
from urllib.parse import urlparse

def is_downloadable(url):
    h=requests.head(url,allow_redirects=True)
    header=h.headers
    content_type=header.get('content-type')
    if 'text'in content_type.lower():
        return False

    if'html' in content_type.lower():
        return False
    return True

def get_filename_from_cd(cd):
    a=urlparse(cd)
    return os.path.basename(a.path)

def marvellousDownload(url):
    allowed=is_downloadable(url)

    if allowed:
        try:
            res=request.get(url,allow_redirects=True)
            filename=get_filename_from_cd(url)
            f=open(filename,"wb")

            for buffer in res.iter_content(1024):
                fd.write(buffer)

            fd.close()
            return True
        except Exception as E:
            return False

    else:
        return False
def main():
    print("marvellous infosystem")
    print("application name",argv[0])

    if(len(argv)==2):
        if(argv[1]=="-h"):
            print("this script used in download file")
            exit()

        if(argv[1]=="-u"):
            print("usage:applicationname")
            exit()

url='https://www.google.com/favicon.ico'
result=marvellousDownload(url)

if result:
    print("file sucessfully download")
else:
    print("failed to download")

if __name__ == "__main__":
    main()