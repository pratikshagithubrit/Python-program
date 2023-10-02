def factor(no):
    if(no<=0):
        return 1
    else:
        return(no*factor(no-1))

ret=factor(4)
print("factorial is",ret)