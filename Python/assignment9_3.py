import os
def filecreatecopy(path,fname):
    flg=os.path.isabs(path)
    if flg == False:
        path=os.path.abspath(path)
        print(path)
        exst=os.path.exists(path)

        if exst:
            f=open(path,"r")
            ctn=f.read()
            f.close()
            f=open(fname,"w+")
            f.write(ctn)
            f.close()
        else:
            print("invalid file")

def main():
    fname=input("give new file to create")
    c=input("give exsiting file name to copy new file")
    try:
        filecreatecopy(c,fname)
    except ValueError:
        print("invalid input datatype")
    except Exception as e:
        print(e)
if __name__ == "__main__":
    main()    
    
    
    
    
    
    
    
    

