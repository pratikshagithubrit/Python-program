def display(n):
    if n>0:
        print(n,end=" ")
        display(n - 1)  
i=5     
display(5)
