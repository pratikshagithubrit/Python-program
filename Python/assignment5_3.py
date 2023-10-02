#instances variables:value1,value2
#instances method:




class  Arithmatic:
    value1=18
    value2=10
    def __init__(self):
        self.value1=0
        self.value2=0

    def AcceptArithmatic(self):
        print("enter the value1")
        self.value1=int(input())

        print("enter the value2")
        self.value2=int(input())

    def AcceptArithmaticInfo(self):
        print("_____your arithmatic information is as below___")
        print("value1 of arithmatic operation",self.value1)
        print("value2 of arithmatic operation",self.value2)

    @classmethod
    def DisplayArithmaticInformation(cls):
        print("welcome to arithmatic operation")
        print("value1 of our arithmatic is",cls.Arithmatic.value1)
        print("value2 of our ariyhmatic is",cls.Arithmatic.value2)

    @staticmethod
    def DisplayOperationsInfo():
        print("please consider below operation information")
        print("according rules of scientist of mathmatics you have to solve below operation")
        
def main():
    value1=Arithmatic()
    value2=Arithmatic()

    print("Accept the first value")
    value1.AcceptArithmatic()

    print("Accept the second value")
    value2.AcceptArithmatic()

    value1.AcceptArithmaticInfo()
    value2.AcceptArithmaticInfo()

    value1=12
    value2=32
    result=value1+value2
    print("addition is",result)

    value1=12
    value2=32
    result=value1-value2
    print("substrction is",result)


    value1=12
    value2=32
    result=value1*value2
    print("multipication is",result)

    value1=12
    value2=32
    result=value1/value2
    print("Division is",result)

if __name__ == "__main__":
    main()