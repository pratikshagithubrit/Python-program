
class numbers():
    def __init__(self):
        self.Size=0
        self.arr=list()
        self.accept()

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

    def average(self):
        Sum=0
        for i in range(0,self.Size):
            Sum=Sum+self.arr[i]

        return (Sum/self.Size)


    def maximum(self):
        max=self.arr[0]
        for i in range(0,self.Size):
            if(self.arr[i]>max):
                max=self.arrr[i]
            

        return max


    def minimum(self):
        min=self.arr[0]
        for i in range(0,self.Size):
            if(self.arr[i]<min):
                min=self.arrr[i]
            

        return min



def main():
    obj=numbers()
    obj.Display()

    output=obj.Summation()
    print("Summation of all element is",output)

    output=obj.average()
    print("average of all element is",output)

    output=obj.maximum()
    print("largest is element is",output)

    output=obj.minimum()
    print("smallest is element is",output)





if __name__ == "__main__":
    main()
