import os
from sys import *
import psutil
import logging as lg

lg.basicConfig(filename='log_12_3.txt',level=lg.DEBUG)
def ProcessDisplay(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    fpath=dirnames+"//"+"running_process.txt"
    fobj=open(fpath,'w')
    fobj.writelines("Process_Name"+","+"P_id"+","+"Process_Username"+"\n")
    for pobj in psutil.process_iter():
        pname=(pobj.name())
        pid=(pobj.pid)
    try:
        pun=(pobj.username())
    except Exception:
        pun="access denied"
    fobj.writelines(str(pname)+","+str(pid)+","+str(pun)+"\n")
    fobj.close()

def main():
    if(len(argv)!=2):
        lg.info("Give proper input,like process name eg-notepad.exe")
        exit()

    try:
        ProcessDisplay(argv[1])
    except ValueError as e:
        lg.warning("invalid input",e)

    except Exception as e:
        lg.warning(e)

if __name__ == "__main__":
    main()