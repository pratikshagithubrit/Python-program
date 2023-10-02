def Add(values):
    Sum=0


    for no in values:
        Sum=Sum+no 
        return Sum

def Addx(values):
    Sum=0
    for i in range(0,len(values),1):
        Sum=Sum+values[i]
        return Sum


def main():
    ans=Addx(1,7,9,4,6,5)
    print("addition is",ans)

if __name__ == "__main__":
    main()
