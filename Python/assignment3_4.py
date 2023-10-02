list = eval(input("enter list"))
element=int(input("enter the number to search"))
length =len(list)
count=0

for i in range(0,length):
    if element == list[i]:
        count+=1

if count == 0:
    print(element,"not found in given list")
else:
    print(element,"has fequency as",count," as given list")


