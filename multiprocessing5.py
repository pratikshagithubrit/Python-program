import multiprocessing
import os
print("demonstrate of multiproceesing")

def fun(no):
    print("process id of fun",os.getpid())
    for i in range(no):
        print(i)

def gun(no):
    print("parent process of gun",os.getpid())
    print("process id of gun",os.getpid())
    for i in range(no):
        print(i)

if __name__ == "__main__":
    print("total cores available",multiprocessing.cpu_count())
    priint("parent.process of main",os.getpid())
    no=3
    result=none
    p1=multiprocessing.Process(target=fun,args=(no,))
    p1=multiprocessing.Process(target=fun,args=(no,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()