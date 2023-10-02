def power(x1):
    return x1

powerfunction = lambda x1:4**2

ans1=power(4)
ans2=powerfunction(4)

print("power using normal function",ans1)
print("power using lambda function",ans2)

print("type of lambda function",type(powerfunction))

