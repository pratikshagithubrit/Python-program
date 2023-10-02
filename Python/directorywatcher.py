import os
from sys import *

def directory_watcher(dir_name):
    print("inside directory watcher method")
    print("name of input dirctory",dir_name)

    for foldername,subfolder,filesnames in os.walk(dir_name):
        print("folder name",+foldername)
        for subf in subfolder:
            print("subfolder name of"+foldername+"is"+subf)
        for fnames in filenames:
            print("file inside folder"+foldername+"is"+fnames)
        print(" ")

def main():
    print("directory watcher application")
    
    if(len(argv)<2):
        print("insufficient argument")
        exit()
    if(argv[1]=="-h"):
        print("this is script will travel directory and display names of all entries")
        exit()

    if(argv[1]=="-u"):
        print("usage:application_name directory_name")
        exit()

    dirctory_watcher(argv[1])
if __name__ == "__main__":
    main()


