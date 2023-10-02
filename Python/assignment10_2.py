from sys import *
import os
import logging as lg
lg.basicConfig(filename="log10_2.txt",level=lg.DEBUG)
def changefileetension(path,ext,cext):
    flg=os.path.isabs(path)
    if flg==False:
        path=os.path.abspath(path)
    exst=os.path.exists(path)

    if exst:
        c=1
        for fd,sbd,f1 in os.walk(path):
            for i in f1:
                if i.split(".")[1]==exst:
                    fn=i.split(".")[0]
                    fn+="."+cext
                    abs=fd+"\\"
                    os.rename(abs+i,abs+fn)
                    c=0
        if c==1:
            lg.info("no files with defined extension found")
    else:
        lg.info("invalid path")

def main():
    if(len(argv)!=4):
        lg.info("give proper input eg(directoryname,exsting file extension(.doc,.txt),changed file extension)")
        exit()

    try:
        ext=argv[2].repalce("."," ")
        cext=argv[3].repalce("."," ")
        changefileextension(argv[1],ext,cext)

    except ValueError:
        lg.warning("invalid input datatype")
    except Exception as e:
        lg.warning(e)

if __name__ == "__main__":
    main()


        
