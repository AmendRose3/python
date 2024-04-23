# 53. Book Recommendation System Based on Keywords: Design an algorithm in Python 
# for a book recommendation system where the keys are book titles and the values are 
# lists of keywords associated with the book. Develop an approach to recommend books 
# based on a user's preferred keywords and optimize the system for handling thousands 
# of books
# Book1": ["adventure", "fantasy", "magic"]


book_details = {}

def add_books(n):
    for _ in range(n):
        name = input("Name of the book: ")
        features_list = []
        for i in range(3):
            feature = input(f"Feature {i+1}: ")
            features_list.append(feature)
        book_details[name] = features_list

def recommend(feature):
    for book, features in book_details.items():
        if feature in features:
            print(f"Book recommended: {book}")

n = int(input("Number of books to add: "))
add_books(n)
feature = input("What type of book are you interested in? ")
recommend(feature)
