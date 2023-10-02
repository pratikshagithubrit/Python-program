from functools import reduce
def main():
    print("enter number of elements you want to enter")
    iSize = int(input())


    Data_Input = []
    print("please enter the data")
    for iCnt in range(0,iSize,1):
        Value =int(input())
        Data_Input.append(Value)


    print("Data is ",Data_Input)



    Data_Filter = list(filter(lambda no:(no%2 == 0),Data_Input))



    print("data after is",Data_Filter)

    Data_map=list(map(lambda no:no**2,Data_Filter))

    print("data after map is",Data_map)

    output = reduce(lambda A,B:A+B,Data_map)
    print("result after reduce is",output)

if __name__ == "__main__":
    main()


