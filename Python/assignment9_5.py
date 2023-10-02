import os
def filewordoccurance(path,c):
    flg=os.path.isabs(path)
    if flg== False:
        path=os.path.abspath(path)
    exst=os.path.exists(path)

    if exst:
        f=open(path,"r")
        ctn=f.read()
        f.close()
        ct=0
        for i in ctn.split():
            if i==c:
                ct+=1
        if ct:
                    print("no.of occurance",ct)
        else:
                    print("no occurance found")
    else:
                print("invalid file")
def main():
    fname=input("give file name")
    c=input("give word to find its occurance")
    try:
        filewordoccurance(fname,c)
    except ValueError:
        print("invalid datatype")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
        