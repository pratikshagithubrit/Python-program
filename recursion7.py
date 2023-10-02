def Add(no):
    ans=0
    while(no>=1):
        ans=ans+no
        no=no-1
    return ans

ret=Add(4)
print("result is",ret)