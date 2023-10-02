#instance variable:name,author
#class variable:noofbooks
#instances method:name,author.noofbooks




class Bookstore:
    noofbooks=0
    def __init__(self):
        self.name=""
        self.author=""

    def CreateStore(self):
        print("enter your name")
        self.name=input()

        print("enter your author")
        self.author=input()

        print("enter the noofbooks")
        self.noofbooks=int(input())

    def DisplayStoreInfo(self):
        print("___your book information is as below___")
        print("name of book holder",self.name)
        print("author of book holder",self.author)
        print("noofbooks in holder",self.noofbooks)

    @classmethod
    def DisplayBookInformation(cls):
        print("welcome to our book store")
        print("name of our book is",cls.Book.name)
        print("written the book author name",cls.Book.author)
        print("noofbooks in our BookStore",cls.Book.noofbooks)

    @staticmethod
    def DisplayKnowledgeInfo():
        print("please consider below knowledge information")
        print("according rules of author of india you have submit below document")
        print("1.clear and recent passport size photo")
        print("2.liabrary card")

    

def main():
        object1=Bookstore()
        object2=Bookstore()

        print("creating the first bookstore")
        object1.CreateStore()

        print("creating the second bookstore")
        object2.CreateStore()
        
        object1.DisplayStoreInfo()
        object2.DisplayStoreInfo()

        
        

        #print("book of {} after increment {}".format(object1.name,object1.author))


if __name__ == "__main__":
    main()


