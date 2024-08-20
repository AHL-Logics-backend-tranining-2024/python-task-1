# Yasser_Sharabati.py
# This file is a template and only an example. Please customize as needed.


# Step 1: Initialize Book Inventory
# Initialize a list of books, each represented as a dictionary with title, author, availability, and tags.

books = [
    {
        "title": "Python Fundamentals",
        "author": "Ahmed Zayed",
        "availability": True, 
        "tags": ["Programming", "Python", "Basics"]
    },
        {
        "title": "The Art of Coding",
        "author": "Mohammed Ali",
        "availability": False, 
        "tags": ["Coding", "Art", "Creativity"]
    },
        {
        "title": "Data Structures in Python",
        "author": "Yousef Amr",
        "availability": True, 
        "tags": ["Data", "Python", "Intermediate"]
    }
]

# Step 2: Filter Books by Author and Availability
# Create a new list with titles of books where the author's name includes "Mohammed" and availability is True.
# available_books_by_mohammed = [ ... ]
available_books_by_mohammed = []
for book in books:
    if "Mohammed" in book["author"] and book["availability"] == True :
        available_books_by_mohammed.append(book["title"])

print(available_books_by_mohammed)


# Step 3: Analyze Tags with Match Statement
# For each book, use a match statement to check the first tag and print relevant messages.
for book in books:
    match book["tags"][0]:
        case "Programming" | "Coding" | "Data":
            print(f'book "{book["title"]}" is Considered as {book["tags"][0]}.')
        case _:
            print("The tag is unrecognized")
