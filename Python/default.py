def area(Radius,PI=3.14):
    Result=PI*Radius*Radius
    return Result



def main():
    Rvalue=10.5
    PIvalue=3.14

    ans=area(Rvalue,PIvalue)
    print("area of circle is",ans)

    ans=area(Radius=Rvalue,PI=PIvalue)
    print("area of circle is",ans)

    ans=area(10.5)
    print("area of circle is",ans)

    ans=area(Radius=10.5)
    print("area of circle is",ans)

    ans=area(PI=7.10,Radius=10.5)
    print("area of circle is",ans)

if __name__ == "__main__":
    main()
