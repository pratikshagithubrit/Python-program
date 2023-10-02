 Application to find out the maximum number

def Maximum(no1,no2):
    if no1 > no2:
        return no1
    else:
        return no2

def main():
    print("enter first number")
    value1 = input()

    print("enter second number")
    value2 = input()

    ans = Maximum(int(value1),int(value2))

    print("largest number is : ",ans)

if __name__ == "__main":
    main()
