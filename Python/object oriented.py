

class arithematic:
    def __init__(self,A,B):
        self.no1=A
        self.no2=B


    def add(self):
        return self.no1+self.no2


    def sub(self):
        return self.no1-self.no2



def main():
    print("enter first number")
    value1=int(input())

    print("enter second number")
    value2=int(input())

    obj=arithematic(value1,value2)

    ans =obj.add()
    print("addition is",ans)

    ans =obj.sub()
    print("substraction is",ans)

   


if __name__ == "__main__":
    main()
