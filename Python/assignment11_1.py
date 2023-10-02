from sys import *
import os
import hashlib 
import logging as lg
lg.basicConfig(filename="log_11_1.txt",level=lg.DEBUG)

def gen_chksum(path):
    flg=os.path.isabs(path)
    if flg==False:
        path=os.path.abspath(path)
    exst=os.path.exists(path)

    if exst:
        c=1
        for fd,sbd,f1 in os.walk(path):
            for i in f1:
                abs=fd+"\\"+i
                lg.info(hashlib.md5(open)(abs,'rb')).read().hexdigest()
                c=0
            if c==1:
                lg.info("no files found")
    else:
        lg.debug("invalid path")

def main():
    if(len(argv)!=2):
        lg.info("give proper input eg(directory name)")
        exit()

    try:
        gen_chksum(argv[1])

    except ValueError:
        lg.warning("invalid input")

    except Exception as e:
        lg.warning(e)

if __name__ == "__main__":
    main()

