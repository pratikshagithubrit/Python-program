import os
from sys import *
import psutil
import logging as lg
lg.basicConfig(filename="log_12_2.txt",level=lg.DEBUG)

def ProcessDisplay(psname):
    plist=psutil.process_iter()
    pname=[]
    pid=[]
    pun=[]
    pcm=[]
    for p in plist:
        psn=str(p.name()).lower()
        if psname.lower()==psn:
            pname.append(str(p.name()))
            pid.append(str(p.pid))
            try:
                pun.append(str(p.username()))
            except Exception:
                pun.append("access denied")
            try:
                pun.append(str(p.memoryperment()))
            except Exception:
                pcm.append("unable to get memorypercent")

                if(len(pid)>0):
                    fp=open("processinfo.txt",'w')
                    for(i,j,k,l)in zip(pname,pid,pun,pcm):
                        fp.writelines(i+","+j+","+k+","+l+"\n")
                    fp.close()

                else:
                    lg.info("either process not running")

def main():
    if(len(argv)!=2):
        lg.info("give proper input,like process name eg.notepad.exe")
        exit()

    try:
        ProcessDisplay(argv[1])
    except ValueError:
        print(e)
        lg.warning("invalid input")
        

    except Exception as e:
        lg.warning (e)

if __name__ == "__main__":
    main()

                




