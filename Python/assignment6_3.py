class numbers:
    def __init__(self,value):
        self.value=value
        
    def chkprime(self):
        n=self.value
        if(n<=1):
            return False
        if(n<=3):
            return True
        if(n%2==0 or n%3==0):
            return False

    def chkperfect(self):
        n=self.value
        Sum=0
        for i in range(1,n):
            if(n%i==0):
                Sum=Sum+i
        if(Sum==n):
            return True
        else:
            return False

    def Sumfactor(self):
        n=self.value
        Sum1=0
        for i in range(1,n):
            if(n%i==0):
                Sum1=Sum1+i
        return Sum1

    def factor(self):
        x=self.value
        list=[]
        for i in range(1,x+1):
            if x%i==0:
                list.append(i)
        return list


def main():
        list=[]
        num=int(input("enter number"))
        obj1=numbers(num)
        print("number is prime{0}".format(obj1.chkprime()))
        print("number is perfect{0}".format(obj1.chkperfect()))
        print("sumfactor{0}".format(obj1.Sumfactor()))
        list=obj1.factor()
        print("factor are{0}".format(list))
        num=int(input("enter number"))

        obj2=numbers(num)
        print("number is prime{0}".format(obj2.chkprime()))
        print("number is perfect{0}".format(obj2.chkperfect()))
        print("Sumfactor{0}".format(obj2.Sumfactor()))
        list=obj2.factor()
        print("factor are{0}".format(list))
        
        
if __name__ == "__main__":
    main()


