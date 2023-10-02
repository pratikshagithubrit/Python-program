import os
def filedisplay(path):
    flg=os.path.isabs(path)
    if flg == False:
        path=os.path.abspath(path)
    print(path)
    exst=os.path.exists(path)

    if exst:
        f=open(path,"r")
        print(f.read())
        f.close()
    else:
        print("invalid file path")

def main():
    c=input("give file name")
    try:
        filedisplay(c)
    except ValueError:
        print("invalid input datatype")
    except Exception:
        print("invalid input")

if __name__ == "__main__":
    main()

