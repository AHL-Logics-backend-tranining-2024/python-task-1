# Liane Raji

# Step 1
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

print("Initialized Book Inventory:")
for book in books:
    print(f"Title: {book['title']}, Author: {book['author']}, Availability: {book['availability']}, Tags: {book['tags']}")

# Step 2
available_books_by_mohammed = [
    book["title"] for book in books if "Mohammed" in book["author"] and book["availability"]
]

print("\nAvailable Books by Authors Named Mohammed:")
print(available_books_by_mohammed)

# Step 3
for book in books:
    match book["tags"][0]:
        case "Programming" | "Coding" | "Data":
            print(f'The book "{book["title"]}" is related to {book["tags"][0]}.')
        case _:
            print(f'The book "{book["title"]}" has an unrecognized tag: {book["tags"][0]}.')


