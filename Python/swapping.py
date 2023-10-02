

def Substraction(no1,no2):
    ans=0
    ans=no1-no2
    return ans

def Decorated_Function(Function_Name):
    def inner(A,B):
        if(A<B):
            A,B=B,A
        return Function_Name(A,B)
    return inner

def main():
    value1=int(input("enter the first number"))
    value2=int(input("enter the second number"))

    new_Function=Decorated_Function(Substraction)
    print(new_Function(value1,value2))

if __name__ == "__main__":
    main()
