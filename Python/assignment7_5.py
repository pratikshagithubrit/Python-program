import threading
def printval():
    for i in range(51):
        print(i)

def Rprintval():
    for i in range(50,-1,-1):
        print(i)

def main():
    t1=threading.Thread(target=printval, args=())
    t2=threading.Thread(target=Rprintval, args=())

    t1.start()
    t1.join()
    t2.start()
    t2.join()
    
if __name__ == "__main__":
    main()