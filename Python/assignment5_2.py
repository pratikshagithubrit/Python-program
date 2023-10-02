#instances variable:radius,area,circumference
#instances method:accept(),calculatearea(),calculatecircumference(),Display()



class Circle:
    PI=3.14
    def __init__(self):
        self.radius=0.0
        self.area=0.0
        self.circumference=0.0
    def CreateCircle(self):
        print("enter the value of radius")
        self.radius=int(input())

        print("enter the value of area")
        self.area=int(input())

        print("enter the value of circumference")
        self.circumference=int(input())
        
    def DisplayCircleInfo(self):
        print("_____your circle information is as below______")
        print("radius of circle",self.radius)
        print("area of circle",self.area)
        print("circumference of circle",self.circumference)

    @classmethod
    def DisplayCircleInformation(cls):
        print("find out the correct value of Circle")
        print("radius of our circle is",cls.Circle.radius)
        print("area of our circle is",cls.Circle.area)
        print("circumference of our Circle is",cls.Circle.circumference)

    @staticmethod
    def DisplayCircleInfo():
        print("please consider below the Circle information")
        print("according to the rules of mathmatics of scientics you have perform below operation")

    def find_Diameter(radius):
        return 2*radius

    def find_circumference(radius):
        return 2*3.14*radius

    def find_area(radius):
        return 3.14*radius*radius

    r=float(int(input("please enter the radius of circle")))
    Diameter=find_Diameter(r)
    circumference=find_circumference(r)
    area=find_area(r)

    print("\n Diameter of circle=%.2f"%Diameter)
    print("circumferenceof circle=%.2f"%circumference)
    print("area of circle=%.2f"%area)

def main():
    User1=Circle()
    User2=Circle()
    User3=Circle()

    print("accept the radius of circle")
    User1.CreateCircle()

    print("accept the area of circle")
    User2.CreateCircle()

    print("accept the circumference of circle")
    User3.CreateCircle()

    User1.DisplayCircleInformation()
    User2.DisplayCircleInformation()


if __name__ == "__main__":
    main()