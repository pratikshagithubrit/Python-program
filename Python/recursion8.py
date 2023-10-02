def Add(no):
    if(no<=0):
        return 0
    else:
        return(no + Add(no-1))

ret=Add(4)
print("result is",ret)