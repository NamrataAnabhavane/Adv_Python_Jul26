class Book:
    def __init__(self,book_ID,title,author,total_copies):
        self.book_ID = book_ID
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -=1
            print("Book Borrowed Successfully.") 
        else:
            print("No copies available.")

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies +=1
            print("Book Returned Successfully")
        else:
            print("All copies are already in the library.")

    def display_details(self):
        print("Book ID: ", self.book_ID)
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Available Copies: ",f"{self.available_copies}/{self.total_copies}")


book1 = Book (101,"Python Programming","Pavan Kumar",3)

book1.display_details()
book1.borrow_book()
book1.borrow_book()
book1.display_details()
book1.borrow_book()
book1.borrow_book()
book1.return_book()
book1.display_details()