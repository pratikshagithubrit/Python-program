print("demonstarte marvellous infosystem")
Class Demo:
    def __init__(self,value1,value2):
        self.i=value1
        self.j=value2

    def fun(self):
        print("inside function")
        print(self.i,self.j)

    def add(self):
        print(self.i+self.j)

        obj1=Demo(10,20)
        obj1.fun()

        obj2=Demo(30,15)
        obj2.fun()

        obj1.add()
        obj2.add()
        result=obj1.add()+obj2.add()

        print("display addition",result)


