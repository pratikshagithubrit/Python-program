import threading
def evenfactor(number):
    for i in range(1,number+1):
        if number%i==0:
            if(i%2==0):
                print("even number",i)
            
            
def oddfactor(number):
    for i in range(1,number+1):
        if number%i==0:
            if(i%2!=0):
                print("odd number",i)

    

def main():
    
    number=30
    p1=threading.Thread(target =evenfactor, args= (number,))
    p2=threading.Thread(target =oddfactor, args= (number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("exsit of main")

if __name__ == "__main__":
    main()



