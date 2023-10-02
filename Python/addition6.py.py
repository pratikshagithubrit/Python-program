print("application to demonstatr industrial program")

def Addition(value1,value2):
     ans=value1+value2
     return ans
def main():
    print("enter first number : ")
    no1=int(input())
    
    print("enter second number : ")
    no2=int(input())
    
    sum=Addition(no1,no2)

    print("addition is",sum)

if __name__ == "__main__":
    main()
