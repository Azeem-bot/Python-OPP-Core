# Project: Library Book Management System
class Book:
    def __init__(self,title,author,available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("Book borrowed successfully")
        else:
            print("Book not available")

    def return_book(self):
        self.available_copies += 1
        print("Book returned Successfully")

    def display(self):
        print("-----Library Details-----")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Available Copies: {self.available_copies}")

b1 = Book(title="Python",author= "o'reilly",available_copies=2)
b1.borrow()
b1.return_book()
b1.display()