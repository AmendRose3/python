def display_books_before_2000(books):
    print("Books published before the year 2000:")
    for book in books:
        if book['year'] < 2000:
            print("Title:", book['title'])
            print("Author:", book['author'])
            print("Year of Publication:", book['year'])
            print()


num_books = int(input("Enter the number of books: "))
books = []
for i in range(num_books):
    title = input("Enter the title of book {}: ".format(i+1))
    author = input("Enter the author of book {}: ".format(i+1))
    year = int(input("Enter the year of publication of book {}: ".format(i+1)))
    books.append({'title': title, 'author': author, 'year': year})


display_books_before_2000(books)
