



def main():
    try:
        print("enter first number")
        no1=int(input())

        print("enter second number")
        no2=int(input())

    
        ans=no1/no2
        print("division is",ans)

    except ZeroDivisionError:
        print("inside zero division error")

    #except NameError:
        #print("exception occured")

    except ValueError:
        print("inside  value error")

    finally:
        print("inside finally block")

if __name__ == "__main__":
    main()    
        
    