
import time
import multiprocessing
def DisplayEven(no):
    for i in range(1,no,1):
        if(i%2==0):
            print("even number",i)


def DisplayOdd(no):
    for i in range(1,no,1):
        if(i%2!=0):
            print("odd number",i)

def main():
    print("demonstration of parallel programming using multiple processes")
    number=2000
    p1=multiprocessing.Process(target = DisplayEven, args = (number,))
    p2=multiprocessing.Process(target = DisplayOdd, args = (number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("end of main")


if __name__ == "__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("execution time is",end_time-start_time)

