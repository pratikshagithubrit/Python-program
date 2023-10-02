import os
import multiprocessing
def square(no):
    print("PID of worker process{} for the input{}".format(os.getpid(),no))
    return(no*no)

def main():
    print("processes ID of our application is",os.getpid)
    data=[1,2,3,4,5]
    result=[]
  
    pobj=multiprocessing.Pool()
    result=pobj.map(square,data)
    print("result after square operation is",result)
    
    
if __name__ == "__main__":
    main()
