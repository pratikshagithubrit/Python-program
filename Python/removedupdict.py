from sys import*
import os
import hashlib
import time

def DeleteFiles(dict1):
    results = list(filter(lambda x:len(x)>1,dict1.values()))

    icnt=0;

    if len(results)>0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    os.remove(subresult)
            icnt=0
    else:
        print("no duplicate files found")

def hashfile(path,blocksize=1024):
    afile=open(path,'rb')
    hasher=hashlib.md5()
    buf=afile.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=afile.read(blocksize)
    afile.close()

    return hasher.hexdigest()

def findDup(path):
    flag=os.path.isabs(path)

    if flag ==False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    dups={}
    if exists:
        for dirName,subdirs,fileList in os.walk(path):
            print("Current folder is:"+dirName)
            for filen in fileList:
                path=os.path.join(dirName,filen)
                filehash=hashfile(path)

                if filehash in dups:
                    dups[filehash].append(path)

                else:
                    dups[filehash]=[path]
                return dups
    else:
        print("invalid path")

def printResults(dict1):
    results = list(filter(lambda x:len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicates found")
        print("the following files are duplicate")
        for result in results:
            for subresult in result:
                print('\t\t%s'%subresult)
    else:
                print("no duplicate files found")

def main():
    print("_______marvellous infosystem_____")
    print("application name:"+argv[0])

    if(len(argv)!=2):
        print("error:invalid number of arguments")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("this script is used to traverse specific directory and delete duplicates files")
        exit()

    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("Usage:application AbsolutePathOfDirectory Extension")
        exit()

    try:
        arr={}
        startTime=time.time()
        arr=findDup(argv[1])
        printResults(arr)
        DeleteFiles(arr)
        endTime=time.time()

        print('Took %s seconds to evalute'%(endTime-startTime))

    except ValueError:
        print("Error:invalid datatype of input")

    except Exception as E:
        print("Error:invalid input",E)

if __name__ == "__main__":
    main()
