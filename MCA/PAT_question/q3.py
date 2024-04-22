"""
Test3 Question
Create a Python-based Library Management System using Object-Oriented Programming
(OOP) principles to manage both regular and digital books. Begin by defining a
base Book class for handling book details like ID, title, and author. Extend this with
a DigitalBook subclass that adds a file size attribute for digital books. Then, implement
a BookCollection class to manage the book inventory, equipped with methods to add books
and retrieve book titles by a specified author.
Your application should start by reading an integer N, indicating the number of books to
input. For each book, read its ID, title, author, and optionally, file size in MB (for digital
books). Afterward, read an author's name and output titles of all books by that author, each on
a new line.
Construct your system by focusing on proper class design, inheritance, and encapsulation
principles.
Class Definitions
Book Class:
• Create a class named Book that will serve as the base class for all types
of books in the library.
• The Book class should have an initializer method that accepts book ID,
title, and author as arguments and stores them as attributes.
DigitalBook Class:
• Define a class named DigitalBook that inherits from the Book class.
• Extend the initializer method to accept an additional argument for file
size (in MB) specific to digital books.
BookCollection Class:
• Implement a BookCollection class to manage the library's collection of
books.
• Include a method to add books (add_book) to the collection, which should
accept an instance of Book or DigitalBook.
• Implement a method get_titles_by_author(self, author_name) that returns a
list of book titles by the specified author.
Sample Input
4
1
Python Basics
Alice Wonderland
2
Advanced Python
Bob Builder
50mb
3
"""

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

class DigitalBook(Book):
    def __init__(self, book_id, title, author, file_size):
        super().__init__(book_id, title, author)
        self.file_size = file_size

class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_titles_by_author(self, author_name):
        titles = []
        for book in self.books:
            if book.author == author_name:
                titles.append(book.title)
        return titles
def main():
    num_books = int(input("Enter the number of books: "))
    library = BookCollection()

    for _ in range(num_books):
        book_id = input("Enter book ID: ")
        title = input("Enter title: ")
        author = input("Enter author: ")
        file_size = input("Enter file size (leave blank for regular books): ")
        
        if file_size:
            book = DigitalBook(book_id, title, author, file_size)
        else:
            book = Book(book_id, title, author)
        
        library.add_book(book)

    author_name = input("Enter author's name to get their books: ")
    titles = library.get_titles_by_author(author_name)
    if titles:
        print("Books by {}: ".format(author_name))
        for title in titles:
            print(title)
    else:
        print("No books found by {}".format(author_name))


