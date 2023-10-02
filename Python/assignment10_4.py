from sys import *
import os
import logging as lg
lg.basicConfig(filename="log_10_4.txt",level=lg.DEBUG)

def copyfilefilter(path,ndir,ext):
    flg=os.path.isabs(path)
    if flg== False:
        path=os.path.abspath(path)
    exst=os.path.exists(path)

    if exst:
        c=1
        for fd,sbd,f1 in os.walk(path):
            for i in f1:
                if i.split(".")[1]==ext:
                    c=0
        if c==1:lg.info("no files with defined extension")
        else:
            import shutil as sh
            ndir=os.path.dirname(ndir)
            if not os.path.exists(ndir):
                os.makedirs.ndirs(ndirs)
                for fd,sbd,f1 in os.walk(path):
                    for i in f1:
                        if i.split(".")[1]==ext:
                            sh.copy(fd+"\\"+i,npath)
            else:
                lg.info("invalid path given")

def main():
    if(len(argv)!=4):
        lg.info("give proper input eg(directory name,new directory name,file extension for filter(.doc,.txt))")
        exit()

    try:
        ext=argv[3].repalce("."," ")
        copyfilefilter(arg[1],arg[2],ext)

    except ValueError:
        lg.warning("invalid input")
    except Exception as e:
        lg.warning(e)

if __name__ == "__main__":
    main()


