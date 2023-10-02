#application to find out minimum of two numbers
def minimum(no1,no2):
    if no1 > no2:
        return no1
    else:
        return no2

def main():
    print("enter the first number")
    value1=input()
    print("enter the second number")
    value2=input()
    result = minimum(float(value1),float(value2))
    print("smallest no is",result)

if __name__ == "__main__":
    main()



