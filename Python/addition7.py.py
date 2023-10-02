print("application to demonstatr industrial program")

import marvellousmodule
def main():
    print("value of __name__ from main is : ",__name__)
    print("enter first number : ")
    no1=int(input())
    
    print("enter second number : ")
    no2=int(input())
    
    sum=marvellousmodule.Addition(no1,no2)

    print("addition is",sum)

if __name__ == "__main__":
    main()
