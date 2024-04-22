class Book:
    def __init__(self, isbn, title, author, price, genre):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.genre = genre

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            print("Book added successfully!")
        else:
            print("Book with the same ISBN already exists!")

    def display_books(self):
        if self.books:
            print("List of all books:")
            for isbn, book in self.books.items():
                print("ISBN:", isbn)
                print("Title:", book.title)
                print("Author:", book.author)
                print("Price:", book.price)
                print("Genre:", book.genre)
                print()
        else:
            print("No books in the library!")

    def search_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            print("Book found!")
            print("ISBN:", book.isbn)
            print("Title:", book.title)
            print("Author:", book.author)
            print("Price:", book.price)
            print("Genre:", book.genre)
        else:
            print("Book with the given ISBN not found!")

def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System Menu:")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Search for a book by ISBN")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author name: ")
            price = float(input("Enter price: "))
            genre = input("Enter genre: ")
            book = Book(isbn, title, author, price, genre)
            library.add_book(book)
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            isbn = input("Enter ISBN to search: ")
            library.search_book(isbn)
        elif choice == '4':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")

if __name__ == "__main__":
    main()
