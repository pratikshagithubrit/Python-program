class circle:
    def __init__(self):
        self.radius=0.0
        self.area=0.0
        self.circumference=0.0

    def createcircle(self):
        print("enter the value of radius")
        self.radius=int(input())

        print("enter the value of area")
        self.area=int(input())

        print("enter the value of circumference")
        self.circumference=int(input())

    def displaycircleinfo(self):
        print("marvellous infosystem")
        print("radius of circle",self.radius)
        print("area of circle",self.area)
        print("crcumference of circle",self.circumference)
    @classmethod
    def displaycircleinformationn(cls):
        print("________display the correct circle information______ ")
        print("radius of circle",self.cls.radius)
        print("area of circle",self.cls.area)
        print("circumference of circle",self.cls.circumference)

    @staticmethod
    def displaycircledetails():
        print("_____display the circle details__________")
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

    user1=cricle()
    user2=circle()
    user3=circle()

    print("accept the radius of circle")
    user1.createcircle()

    print("accept the area of circle")
    user2.createcircle()

    print("accept the circumference of circle")
    user3.createcircle()


    user1.displaycircleinformationn()
    user2.displaycircleinformationn()
    user3.displaycircleinformationn()





if __name__ == "__name__":
    man()