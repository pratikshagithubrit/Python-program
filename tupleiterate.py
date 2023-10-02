data = (10,21,51,101)
print("output using for")
for no in data:
    print(no,end =" ")
    print()

print("output using for with index")
for i in range(0,len(data)):
    print(data[i],end =" ")
    print()

   
print("output using while with index") 
i=0
while(i< len(data)):
     print(data[i],end =" ") 
     i+=1
print()