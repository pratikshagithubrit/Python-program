from sys import *
import os
import logging as lg
lg.basicConfig(filename="log_10_1.txt",level=lg.DEBUG)
'''logging.debug('this msg should not be log file')
logging.info('so should this')
logging.warning('and this,too')
'''
def changefileextension(path,ext):
    flag=os.path.isabs(path)
    if flag==False:
        path=os.path.abspath(path)
    exst=os.path.exists(path)

    if exst:
        c=1
        for fd,sbd,f1 in os.walk(path):
            for i in f1:
                if i.split(".")[1]==ext:
                    lg.info(i)
                    c==0
        if c==1:
            lg.info("no files with defined extension found")
        else:
            lg.debug("invalid path")

def main():
    if (len(argv)!=3):
        lg.info("give proper input,eg(directory name,file extension(.doc,.txt))")
        exit()

    try:
        ext=argv[2].repalce("."," ")
        changefileextension(argv[1],ext)

    except ValueError:
        lg.warning("invalid input")

    except Exception as e:
        lg.warning(e)

if __name__ == "__main__":
    main()


