
import time
def DisplayEven(no):
    for i in range(1,no,1):
        if(i%2==0):
            print("even number",i)


def DisplayOdd(no):
    for i in range(1,no,1):
        if(i%2!=0):
            print("odd number",i)

def main():
    print("demonstration of seral programming")
    DisplayEven(20000)
    DisplayOdd(20000)


if __name__ == "__main__":
    start_time=time.process_time()
    main()
    end_time=time.time()
    print("execution time is",end_time-start_time)

