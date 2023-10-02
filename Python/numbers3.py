
class numbers():
    def __init__(self):
        self.Size=0
        self.arr=list()

    def Accept(self):
        print("how many element you want")
        self.Size=int(input())

        print("please enter the elements")
        value=0
        for i in range(0,self.Size):
            value=int(input())
            self.arr.append(value)


    def Display(self):
        print("element from list are")
        for i in range(0,self.Size):
            print(self.arr[i])

    def Summation(self):
        Sum=0
        for i in range(0,self.Size):
            Sum=Sum+self.arr[i]

def main():
    obj=numbers()
    obj.Accept()
    obj.Display()

    output=obj.Summation()
    print("Summation of all element is",output)




if __name__ == "__main__":
    main()
