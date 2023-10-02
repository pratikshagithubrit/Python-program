from sys import *
import webbrowser
import re
import urllib.request

def isconnected():
    try:
        urllib.urlopen("http://216.58.192.142",timeout=1)
        return True
    except urllib.URLError as err:
        return False

def Find(string):
    url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|]!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',string)
    return url

def weblauncher(path):
    with open(path)as fp:
        for line in fp:
            print(line)
            url=Find(line)
            print(url)
            for str in url:
                webbrowser.open(str,new=2)

def main():
    print("marvellous infosystem")

    print("application name"+argv[0])

    if(len(argv)!=2):
        print("Error:invalid number of argument")
        exit()

    if(argv[1]=="-h"):
        print("the script is used URLwhich written in one file")
        exit()

    if(argv[1]=="-u"):
        print("usage:applicationname nameoffile")
        exit()

    try:
        connected=isconnected()

        if connected:
            weblauncher(argv[1])
        else:
            print("unable to connect internet")

    except ValueError:
        print("error:invalid input")

    except Exception as E:
        print("error:invalid input",E)

if __name__ == "__main__":
    main()





