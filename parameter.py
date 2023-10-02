def add1(no1,no2):
    print("value is no1",no1)
    print("value is no2",no2)
    return no1+no2


def sub1(no1,no2):
    print("value is no1",no1)
    print("value is no2",no2)
    return no1-no2


def main():
    ans=0
    ans=add1(10,11)
    print("addition is",ans)


    ans=sub1(no2=10,no1=11)
    print("substraction is",ans)

    ans=sub1(no2=11,no1=10)
    print("substraction is",ans)


if __name__ == "__main__":
    main()
