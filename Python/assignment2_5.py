num = 5
if num > 1:
    for i in range(2,int(num/2)+1):
        if(num % i) == 0:
            print(num,"is not prime number ")
        else:
            print(num,"is prime number")