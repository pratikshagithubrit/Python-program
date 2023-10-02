
from sys import *
import os
import hashlib
import logging as lg
lg.basicConfig(filename='log_11_2.txt',level=lg.DEBUG)

def Dup_by_ckecksum(path):
    flg=os.path.isabs(path)
    if flg == False:
        path=os.path.abspath(path)
    exst=os.path.exists(path)

    if exst:
        c=1
        file_chk=dict()
        for fd,sbd,f1 in os.walk(path):
            for i in f1:
                abs=fd+"\\"+i
                v1=(hashlib.md5(open(abs,'rb').read()).hexdigest())
        flipped={}
        for key,value in file_chk.items():
            if value not in flipped:
                flipped[value]=[key]
            else:
                flipped[value].append(key)

        f=open("Log.txt","w+")
        for i in flipped:
            v=flipped[i]
            if len(v)>1:
                for i in v:
                    f.write(i+"\n")
                s="-"*5
                f.write(i+"\n")
        f.close()
        if c==1:
            lg.info("no files found")
        else:
            lg.debug("invalid path")

def main():
    if(len(argv)!=2):
        lg.info("give proper input,eg(directory name)")
        exit()

    try:
        Dup_by_chksum(argv[1])

    except ValueError:
        lg.warning("invalid input datatype")

    except Exception as e:
        lg.warning(e)
                

if __name__ == "__main":
    main()
