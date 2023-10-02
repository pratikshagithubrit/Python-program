import os
def filecompare(path,fname):
    flg=os.path.isabs(path)
    if flg == False:
        path=os.path.abspath(path)
    exst=os.path.exists(path)

    if exst:
        f=open(path,"r")
        ctn1=f.read()
        f.close()
        f=open(fname,"r")
        ctn2=f.read()
        f.close()

        if ctn1==ctn2:
            print("success")
        else:
            print("failure")
    else:
        print("invalid file")

def main():
    fname=input("give first file name")
    c=input("give second file name to compare to first")
    try:
        filecompare(fname,c)
    except ValueError:
        print("invalid input")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()