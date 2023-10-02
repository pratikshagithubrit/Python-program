l=[13,5,45,7,4,56,10,34,2,5,8]
mylist=[13,5,7,2,5]
total=sum(mylist)
prime=[]
for i in l:
    c=0
    for j in range(1,i):
        if i%j==0:
            c=c+1
    if c== 1:
        prime.append(i)
print("sum of all in given mylist",total)
print("prime number are",prime)







    







