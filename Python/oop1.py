
class Arithematic:
    def __init__(self,A,B):
        print("inside init method")
        self.no1=A
        self.no2=B

    def Addition(self):
        ans=self.no1+self.no2
        return ans


    def substraction(self):
        ans=self.no1-self.no2
        return ans



def main():
    print("inside main method")

    obj=Arithematic(11,10)
    output=obj.Addition()
    print("Addition is",output)
    output=obj.substraction()
    print("substraction is",output)


if __name__ == "__main__":
    print("inside starter")
    main()