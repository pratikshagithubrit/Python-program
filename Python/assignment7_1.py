import threading
def DisplayEven(no):
    for i in range(1,10):
        if(i%2==0):
            print("even number",i)

def DisplayOdd(no):
    for i in range(1,10):
        if(i%2!=0):
            print("odd number",i)

def main():
    print("demonstation of parallel programming using multiple processes")
    number=10
    p1=threading.Thread(target=DisplayEven,args=(number,))
    p2=threading.Thread(target=DisplayOdd,args=(number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("end of main")

if __name__ == "__main__":
    main()
    