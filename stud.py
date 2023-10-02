#instance variable:name,rollno,add
#instance method:createstud(),dispalystudonfo()

class stud_Account:
    stud_name="savitribai phule pune uni"
    attendence=30
    def __init__(self):
        self.name=" "
        self.rollno=0
        self.address=" "

    def createstud(self):
        print("enter your name")
        self.name=input()
        print("enter your rollno")
        self.rollno=int(input())
        print("enter your address")
        self.address=input()

    def displayinfo(self):
        print("____your student information is as below_______")
        print("name of student",self.name)
        print("rollno of student",self.rollno)
        print("adderess of student",self.address)

    def displaystudinfo(cls):
        print("welcome to college")
        print("name of oue stud is",cls.stud_name)
        print("attendence of our stud is",cls.attendence)

def main():
    print("name of student",stud_Account.stud_name)
    print("daily student present in attendence on fixed days",stud_Account.attendence)
    student1=stud_Account()
    student2=stud_Account()

    print("creating first account")
    student1.createstud()

    print("creating second account")
    student2.createstud()

    student1.displayinfo()
    student2.displayinfo()

    student1.displaystudinfo()
    student2.displaystudinfo()
    




if __name__ == "__main__":
    main()