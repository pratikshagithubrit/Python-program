
import arithmaticmodule as arithmatic
def main():
    print("value of __name__from main is",__name__)
    num1=int(input("enter the first number"))
    num2=int(input("enter the second number"))
    

    add=arithmatic.arithmaticmodule(num1,num2)
    print("addition is",add)

    sub=arithmatic.arithmaticmodule(num1,num2)
    print("substraction is",sub)

    mult =arithmatic.arithmaticmodule(num1,num2)
    print("multiplication is",mult)

    div=arithmatic.arithmaticmodule(num1,num2)
    print("division is",div)

if __name__ == "__main__":
    main()