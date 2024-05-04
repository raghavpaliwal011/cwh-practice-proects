#library management system

class library :
    def __init__(self,listofbooks):
        self.books = listofbooks
    def displayavailablebooks(self):
        print ("books present in this library are:")
        for book in self.books:
            print()
            print ("\t" +book)
            
    def borrowbook(self,bookname):
        if bookname in self.books:
            print (f"you have been issued {bookname}. please keep it safe , learn from it and return it in 30 days")
            self.books.remove(bookname)
            return True
        else:
            print ("sorry this book has has already been issued to someone else please wait until the book is returned")
            return False
        
    def returnbook(self,bookname):
        self.books.append(bookname)
        print (" THANKS for returning this book we hope you enjoyed this book keeep learning and have a good day ahead")
class student :
    def __init__(self):
        self.book= input ("enter the name of the book you want to borrow.")
        return self.book

    def requestbook(self):
        self.book = input ("enter the name of the book you want to return.")
        return self.book
    

if __name__ == "__main__":
    centrallibrary = library(["algorithms","light pollution","universe in a nutshell","how a rocket works"])
    student = student()
    #centrallibrary.displayavailablebooks()
    while (True):
        welcomemsg = '''===welcom to central library===
        please choose an option:
        1. listening all the books
        2. request a book
        3. return a book

        4. exit the library'''
        a = int (input("enter a choice :"))
        if a == 1:
            centrallibrary.displayavailablebooks()
        elif a == 2:
            centrallibrary.borrowbook()
        elif a == 3:
            centrallibrary.returnbookbook()
        elif a == 4:
            print ("thanks for choosing central library ! have a great day ahead")
            exit()
        else:
            print ("invalid choice!")
        print (welcomemsg)