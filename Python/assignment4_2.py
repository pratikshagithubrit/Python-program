def mult(no1,no2):
    return no1*no2

multfunction = lambda A,B:A*B

ans1=mult(4,3)
ans2=multfunction(4,3)

print("multiplication using normal function",ans1)
print("multiplication using lambda function",ans2)

print("type of lambda function",type(multfunction)

