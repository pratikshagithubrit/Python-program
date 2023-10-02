print("demonstrate of set")

data ={11,21,51,10,21,11}
data1 = {11,90.13,"true","hello"}
print("first set data",data)
print("length of data",len(data))
print("data is hetrogenous",data1)
print("data is ordered",data1)
#print("data at index 2",data1{2})
print("data with unique element",data1)

print("set is mutable")
data.add(211)
print("data after insertion",data)

data.remove(211)
print("data after removal",data)

data.discard(201)
print("data after removal",data)