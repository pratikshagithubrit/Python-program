def check_number(x):
    if x>0:
        print("number is positive")
    elif x<0:
        print("number is negative")
    elif x==0:
        print("number is zero")

x=(int(input("enter the number")))
check_number(x)