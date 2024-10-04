class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
    
    def return_book(self):
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title
            return book
        return None
    
    def lend_book(self, title):
        book = self.find_book(title)
        if book and book.check_out():
            print(f"Book '{title}' has been lent out.")
        else:
            print(f"Book '{title}' is not available.")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.return_book()
            print(f"Book '{title}' has been returned.")
        else:
            print(f"Book '{title}' not found in the library.")

library = Library()

while True:
    action = input("Enter action (add, lend, return, search, exit): ").lower()
    if action == "exit":
        break

    try:
        if action == "add":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(Book(title, author))
            print(f"Added book '{title}'")
        elif action == "lend":
            title = input("Enter book title: ")
            library.lend_book(title)
        elif action == "return":
            title = input("Enter book title: ")
            library.return_book(title)
        elif action == "search":
            title = input("Enter book title: ")
            book = library.find_book(title)
            if book:
                availability = "available" if book.is_available else "not available"
                print(f"'{title}' by {book.author} is {availability}")
            else:
                print(f"Book '{title}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Library system closed.")