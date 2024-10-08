
books = [
    {
        "Title": "Python Fundamentals", 
        "Author": "Ahmed Zayed",
        "Availability": True,
        "Tags": ["Programming", "Python", "Basics"]
    },
    {
        "Title": "The Art of Coding",
        "Author": "Mohammed Ali",
        "Availability": False, 
        "Tags": ["Coding", "Art", "Creativity"]
    },
    {
        "Title": "Data Structures in Python",
        "Author": "Yousef Amr",
        "Availability": True,
        "Tags": ["Data", "Python", "Intermediate"]
    }
]


# Step 2: Filter Books by Author and Availability
# Create a new list with titles of books where the author's name includes "Mohammed" and availability is True.
# available_books_by_mohammed = [ ... ]

available_books_by_mohammed = []
for book in books:
    if "Mohammed" in book["Author"] and book["Availability"] == True :
        available_books_by_mohammed.append(book["Title"])

print(available_books_by_mohammed)
             


# Step 3: Analyze Tags with Match Statement
# For each book, use a match statement to check the first tag and print relevant messages.
for book in books:
    match book["Tags"][0]:
        case "Programming" | "Coding" | "Data":
            print(f'The book "{book["Title"]}" is related to {book["Tags"][0]}.')
        case _:
            print("The tag is unrecognized")

            


