import os
import psutil
import time
from sys import *
import os

def ProcessDisplay(log_dir="marvellous"):
    listprocess = []

    if not os.path.exsits(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir,"marvellousLog%s.log")
    f=open(log_path +'w')
    f.write(separator +"\n")
    f.write("marvellous infosystem process logger:"+"time")
    f.write(separator,"\n")

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            vms=proc.memory_info().vms/(1024 * 1024)
            pinfo['vms']=vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n"%element)

def main():
    print("_____marvellous infosystem by pratiksha pawar________")
    print("Application name:" + argv[0])

    if(len(argv)!=2):
        print("Error:Invalid number of argument")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"):
        print("this script is used log record of running processess")
        exit()

    if(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage:applicationname absolutepath_of_directory")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error:invalid datatype of input")


    except Exception:
        print("Error:Invalid input")

if __name__ == "__main__":
    main()
    


