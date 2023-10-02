#instance variable:name,amount,adderss accountno
#instance method:createaccount(),displayaccountinfo
#class variable
class Bank_Account:

    Bank_name="HDFC bank pvt ltd"
    ROI_On_FD=6.7
    def __init__(self):
        self.name=""
        self.amount=0
        self.address=""
        self.accountno=0

    def CreateAccount(self):
        print("enter your name")
        self.name=input()

        print("enter your intial amount")
        self.amount=int(input())

        print("enter your address")
        self.address=input()

        print("enter your account number")
        self.accountno=int(input())

    def DisplayAccountInfo(self):
        print("_____your account information is as below____")
        print("name of account holder",self.name)
        print("account name",self.accountno)
        print("address of account holder",self.address)
        print("current amount in account",self.amount)

    @classmethod
    def DisplayBankInformation(cls):
        print("welcome to banking console")
        print("name of our bank is",cls.Bank_name)
        print("rate of intrest we offer on fixed deposite is",cls.ROI_On_FD)
            
    @staticmethod
    def DisplayKYCInfo():
        print("please consider below KYC information")
        print("according to the rules of goverment of india you have to submit below document")
        print("1:clear and recent passport size photo")
        print("2:photo of aadhar card")
        print("3:photo of pan card")

    def Deposite(self,value):
        self.amount=self.amount+value

    def Withdraw(self,value):
        self.amount=self.amount-value

def main():
    print("_________________________________")
    print("_______Banking application______________")
    print("______________")
    print("____________calling Static method to display KYCinfo__________")
    Bank_Account.DisplayKYCInfo()
    print("_________________________")
    print("____________accessing the class variables from main_________")
    print("______________")
    print("name of bank",Bank_Account.Bank_name)
    print("rate of interest on fixed deposite",Bank_Account.ROI_On_FD)
    print("______________")
    print("_____calling the class method to display Bank information__________ ")
    print("___________")
    Bank_Account.DisplayBankInformation()
    print("_______________________")
    print("_________creating the object of class______")
    print("________________")

    User1 = Bank_Account()
    User2 = Bank_Account()

    print("_____________________________")
    print("creating the first account")
    print("________________________")
    print("________________________")
    print("_________ennter details for first account holder______")
    print("_____________")
    

    
    User1.CreateAccount()
    print("_________________")
    print("creating the second account")
    print("_________________")
    print("______________")
    print("_________ennter details for second account holder______")
    User2.CreateAccount()
    print("______________")
    User1.DisplayAccountInfo()
    print("_________calling instance method to display information of second account_____")
    User2.DisplayAccountInfo()
    print("________depositing 500 in User1_______")

    User1.Deposite(500)
    print("________depositing 100 in User2_______")
    User2.Deposite(100)
    
    print("amount of User1 after deposite".format(User1.name,User1.amount))
    print("amount of User2 after deposite".format(User2.name,User2.amount))
    print("________Withdraw 200 in User1____")

    
    User1.Withdraw(200)
    print("___________Withdraw 302 in User2_____")
    User2.Withdraw(302)
    print("amount of {} after Withdraw is {}:".format(User1.name,User1.amount))
    print("amount of {} after Withdraw is {}:".format(User2.name,User2.amount))

    print("________________")
    print("___________end of banking application_________")
    print("_______________")
    
    


if __name__ == "__main__":
    main()