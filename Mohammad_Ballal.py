# Define a list of books, where each book is represented as a dictionary containing its title, author, availability, and tags.
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


# Initialize an empty list to store the titles of available books by authors named Mohammed.
available_books_by_mohammed= []

# find books by "Mohammed" that are available.
for book in books:
    # Check if the author's name contains "Mohammed" and if the book is available.
    if "Mohammed" in book['author'] and book['availability']:
        available_books_by_mohammed.append(book['title'])

# Print the list of available books by Mohammed.
print(f"Available book by Mohammed :{available_books_by_mohammed}")


# Print the list of available books by Mohammed in another way.
"""
print("Available book by Mohammed :")
for book in available_books_by_mohammed:
    print(f"{book} \n") 
"""

# analyze primary tag using the match statement.
for book in books:
    match book['tags'][0]:
        # Check if the first tag is "Programming", "Coding", or "Data" and print a message.
        case "Programming" | "Coding" | "Data" :
            print(f"{book['title']} is related to {book['tags'][0]}")

        # Handle any unrecognized primary tags.
        case _:
            print(f"{book['title']} has an unrecognized primary tag {book['tags'][0]}")


# another way to analyze primary tag using the if statement.
"""
for book in books:
    if book['tags'][0] in ["Programming", "Coding", "Data"]:
        print(f"{book['title']} is related to {book['tags'][0]}")
    else:
        print(f"{book['title']} has an unrecognized primary tag {book['tags'][0]}")
"""


            



