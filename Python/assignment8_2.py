def display(n):
    if(n>0):
        display(n-1)
        print(n,end=" ")  
i=5     
display(5)
