from sys import*
import os
import hashlib

def hashfile(path,blocksize=1024):
    fd=open(path,'rb')
    hasher=hashlib.md5()
    buf=fd.read(blocksize)

    while len(buf)>0:
        hasher.update(buf)
        buf=fd.read(blocksize)
    fd.close()

    return hasher.hexdigest()

def FindDuplicate(path):
    flag=os.path.isabs(path)

    if flag == False:
        path = os.path.abspath(path)

    exists=os.path.isdir(path)

    dups={}
    if exists:
        for dirName,subdirs,fileList in os.walk(path):
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

def PrintDuplicate(dict1):
    results = list(filter(lambda x:len(x)>1,dict1.values()))

    if len(results)>0:
        print("Duplicates Found")

        print("the following files are identical")

        icnt=0;
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    print('\t\t%s'%subresult)
        else:
            print("no duplicate files found")

def main():
    print("____marvellous infosystem_________")
    print("application name"+argv[0])

    if(len(argv)!=2):
        print("Error:invalid number of argments")
        exit()

    if(argv[1]=="-h")or(argv[1]=="-H"):
        print("the script is used to traverse specific directory and display sizes of files")
        exit()

    if(argv[1]=="-u")or(argv[1]=="-U"):
        print("usage:application AbsolutePathOfDirectory Extension")
        exit()
        
    
    try:
        arr={}
        arr=FindDuplicate(argv[1])
        PrintDuplicate(arr)

    except ValueError:
        print("Error:invalid datatype of input")

if __name__ == "__main__":
    main() 
    
