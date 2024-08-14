# FIRST-NAME_LAST-NAME.py
# This file is a template and only an example. Please customize as needed.
# Step 1: Initialize Book Inventory
# Initialize a list of books, each represented as a dictionary with title, author, availability, and tags.
books = [
    {"Title": "Python Fundamentals", "Author": "Ahmed Zayed", "Availability": True, "Tags": ["Programming", "Python", "Basics"]},
    {"Title": "The Art of Coding", "Author": "Mohammed Ali", "Availability": False, "Tags": ["Coding", "Art", "Creativity"]},
    {"Title": "Data Structures in Python", "Author": "Yousef Amr", "Availability": True, "Tags": ["Data", "Python", "Intermediate"]}
]

# Step 2: Filter Books by Author and Availability
# Create a new list with titles of books where the author's name includes "Mohammed" and availability is True.
# available_books_by_mohammed = [ ... ]
available_books_by_mohammed = []
for book in books:
    if "Mohammed" in book["Author"] and book["Availability"]:
        available_books_by_mohammed.append(book["Title"])
        
print(type(available_books_by_mohammed))
print(available_books_by_mohammed)

# Step 3: Analyze Tags with Match Statement
# For each book, use a match statement to check the first tag and print relevant messages.
for book in books:
    match book["Tags"][0]:
        case "Programming":
            print(f'The book "{book["Title"]}" is related to programming.')
        case "Coding":
            print(f'The book "{book["Title"]}" is related to coding.')
        case "Data":
            print(f'The book "{book["Title"]}" is related to data.')
        case _:
            print ( f'the book "{book["Title"]}" is not recognized ')