import os
def directorychecker(path):
    flg=os.path.isabs(path)
    if flg == False:
        path=os.path.abspath(path)
    exst=os.path.isdir(path)

    if exst:
        for fd,sbd,f1 in os.walk(path):
            print("folder",fd)
            for i in sbd:
                print("subfolder",i)
            for i in f1:
                print("\n")
            print(" ")
    else:
        print("invalid directory path")

def main():
    c=input("give directory name")
    try:
        directorychecker(c)
    except ValueError:
        print("invalid input datatype")
    except Exception:
        print("invalid input")

if __name__ == "__main__":
    main()

