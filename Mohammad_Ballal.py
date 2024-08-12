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

available_books_by_mohammed= []

for book in books:
    if "Mohammed" in book["author"] and book["availability"]:
        available_books_by_mohammed.append(book["title"])

print(f"Available book by Mohammed :{available_books_by_mohammed}")

"""
print("Available book by Mohammed :")
for book in available_books_by_mohammed:
    print(f"{book} \n") 
"""

for book in books:
    match book["tags"][0]:
        case "Programming" | "Coding" | "Data" :
            print(f"{book["title"]} is related to {book["tags"][0]}")

        case _:
            print(f"{book["title"]} has an unrecognized primary tag {book["tags"][0]}")

"""
for book in books:
    if book["tags"][0] in ["Programming", "Coding", "Data"]:
        print(f"{book["title"]} is related to {book["tags"][0]}")
    else:
        print(f"{book["title"]} has an unrecognized primary tag {book["tags"][0]}")
"""


            



