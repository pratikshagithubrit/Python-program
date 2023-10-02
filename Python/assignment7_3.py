import threading
def evenfactor(no):
    sum=0
    for i in range(1,no):
        if no%i==0 and i%2==0:
            sum=sum+i
            print("even",sum)
        
def oddfactor(no):
    sum=0
    for i in range(1,no):
        if no%i==0 and i%2!=0:
            sum = sum+i
            print("odd",sum)


def main():
    no=int(input("enter number"))
    t1=threading.Thread(target =evenfactor , args=(no,))
    t2=threading.Thread(target =oddfactor ,args=(no,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("end of main")

if __name__ == "__main__":
    main()