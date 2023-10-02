#instances variable:no1,no2
#instance method:Fun(),Gun()
#class variable:no1,no2
#class method:DisplayDemoInformation

class Demo:
    Demo_object1=(11,21)
    Demo_object2=(51,101)
    def __init__(self):
        self.no1=0
        self.no2=0

    def createobject(self):
        print("enter your no1 value")
        self.number1=int(input())

        print("enter your no2 value")
        self.number2=int(input())

    def DisplayObjectInfo(self):
        print("________your object information is as below______ ")
        print("number1 of object",self.number1)
        print("number2 of object",self.number2)

    @classmethod
    def DisplayDemoInformation(cls):
        print("welcome to demo console")
        print("no1 of our Demo is",cls.Demo_object1)
        print("no2 of our Demo is",cls.Demo_object2)
def main():
    print("object1 of Demo",Demo.Demo_object1)
    print("object2 of Demo",Demo.Demo_object2)
    Demo.DisplayDemoInformation()
    object1=Demo()
    object2=Demo()

    print("creating the first object")
    object1.createobject()

    print("creating the second object")
    object2.createobject()

    object1.DisplayObjectInfo()
    object2.DisplayObjectInfo()

if __name__ == "__main__":
    main()