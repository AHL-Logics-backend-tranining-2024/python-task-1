
# Step 1: Initialize a list of books, each represented as a dictionary with title, author, availability, and tags.
books = [
    # Dictionary with Multiple Properties
    {
        "title": "Python Fundamentals",
        "author": "Ahmed Zayed",
        "availability":True,
        "tags": ["Programming","Python","Basics"]
    },
    {
        "title": "The Art Of Coding",
        "author": "Mohammed Ali",
        "availability":False,
        "tags": ["Coding","Art","Creativity"]
    },
    {
        "title": "Data Structures In Python",
        "author": "Yousef Amr",
        "availability":True,
        "tags": ["Data","Python","Intermediate"]
    },
]

#############################################################

# Step 2: Filter Books by Author and Availability
available_books_by_mohammed = [book["title"] for book in books if "Mohammed" in book["author"] and book["availability"]];

# Print
print(F"available books by mohammed is : {available_books_by_mohammed}");
# Output :[available books by mohammed is : []]


# Check if the list is empty
if not available_books_by_mohammed :
    print("The list is empty, nothing to analyze.")
else:
    for ob in available_books_by_mohammed:
        print(ob);

# Output :[The list is empty, nothing to analyze.]



#############################################################

# Step 3: Analyze Tags with Match Statement
for book in books:
   # Create a Variable to Store Data from a Book Object
   first_tag = book["tags"][0];

   match first_tag:
       # Check if the first tag is "Programming" and print a message.
       case "Programming":
           print(f"The book {book['title']} is related to {first_tag}.")
       # Check if the first tag is "Coding" and print a message.
       case "Coding":
           print(f"The book {book['title']} is related to {first_tag}.")
       # Check if the first tag is "Data" and print a message.
       case "Data":
           print(f"The book {book['title']} is related to {first_tag}.")
       # Handle any unrecognized tags and print the message.
       case _:
           print(f"'{book['title']}' has an unrecognized tag: {first_tag}.")

# Output when all tags is defined
""" 
The book Python Fundamentals is related to Programming.
The book The Art Of Coding is related to Coding.
The book Data Structures In Python is related to Data.
"""

# When Replace between tags[0] and tags[1] at list  "tags": ["Python","Programming","Basics"]
""" 
'Python Fundamentals' has an unrecognized tag: Python.
The book The Art Of Coding is related to Coding.
The book Data Structures In Python is related to Data.
"""