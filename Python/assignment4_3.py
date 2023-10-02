num=[4,34,36,76,68,24,89,23,86,90,45,70]
check=filter(lambda num:70<=90,num)
Doubles =list(map(lambda num:num**2,num))
product=reduce(lambda A,B:A*B)
def main():
    print("plese enter the you want to store")
    iSize=int(input())
    Data_Input=[]
    print("please enter the data")
    for icnt in range(70<=90):
        value=int(input())
        Data_append.append(value)

    print("Data is",Data_Input)
    Data_Filter=list(Filter(num,Data_Input))
    print("data after filter is",Data_Filter)
    Data_map=list(map,10,Data_Filter)
    output=reduce(product,Data_map)
    print("result after reduce is",output)

    if __name__ == "__main__":
        main()
