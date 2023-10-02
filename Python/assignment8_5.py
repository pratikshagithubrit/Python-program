def sumofdigits(inputnumber):
    if(inputnumber==0):
        return 0
    else:
        return(inputnumber%10+sumofdigits(int(inputnumber/10)))

inputnumber=int(input("please provide input number"))
print("sum of",inputnumber,"is",sumofdigits(inputnumber))
#Sum(879)
#num=int(input("enter number"))
#total=sum(num)
#print("sum is",total)
    
              
