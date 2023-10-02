

def Display(no):
    if(no>0):
    
        no=no-1
        Display(no)#recursive call
        print(no)
    
Display(4)