from sys import *
import os
import hashlib

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(path):
    flag=os.path.isabs(path)
    if flag == false:
        path =os.path.abspath(path)
    exsits=os.path.isdir(path)

    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            print("current folder is"+dirName)
            for filen in fileList:
                path=os.path.join(dirName,filen)
                filehash=hashfile(path)
        print("Error:invalid number of arguments")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("this script is used to travese specific dirctory")
        exit()

    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("usage:applicationName AbsolutePathofDirectory")
        exit()

    try:
        DirectoryWatcher(Argv[1])

    except ValueError:
        print("Error:invalid datatype of input")

    except Exception:
        print("Error:invalid input")

def main():

