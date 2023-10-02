from sys import *
import os
import shutil as sh
import logging as lg
lg.basicConfig(filename="log10_3.txt",level=lg.DEBUG)

def copydirectory(path,dir):
    flg=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)
    exst =os.path.exists(path)

    if exst:
        sh.copytree(path,ndir)
    else:
        lg.info("invalid path")

def main():
    if(len(argv)!=3):
        lg.info("give proper input,eg(directoryname,new directory name)")
        exit()
    try:
        copydirectory(argv[1],argv[2])
    except ValueError:
        lg.warning("invalid input")
    except Exception as e:
        lg.warning(e)

if __name__ == "__main__":
    main()
