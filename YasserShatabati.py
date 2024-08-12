# Yasser_Sharabati.py
# This file is a template and only an example. Please customize as needed.


# Step 1: Initialize Book Inventory
# Initialize a list of books, each represented as a dictionary with title, author, availability, and tags.

books= [
    {
        'title':'The New Psychology of Success',
        'author':'Carol S. Dweck',
        'availability':True,
        'tags':['Psychology','personal-dev']
    },
    {
        'title':'The Selfish Gene',
        'author':'Mohammed',
        'availability':True,
        'tags':['Psychology','science']
    },
    {
        'title':'The Alchemist',
        'author':'Mohammed',
        'availability':False,
        'tags':['philosophy','science','chemistry']
    },
     {
        'title':'A Brief History of Humankind',
        'author':'Yuval Noah Harari',
        'availability':False,
        'tags':['History']
    },
    {
        'title':'To Kill a Mockingbird',
        'author':'Mohammed',
        'availability':True,
        'tags':['novel','morality']
    }   
]

# Step 2: Filter Books by Author and Availability
# Create a new list with titles of books where the author's name includes "Mohammed" and availability is True.
# available_books_by_mohammed = [ ... ]
available_books_by_mohammed = [book['title'] for book in books if book['author'] == 'Mohammed' and book['availability'] == True]

print (available_books_by_mohammed)


# Step 3: Analyze Tags with Match Statement
# For each book, use a match statement to check the first tag and print relevant messages.

for book in books:
    print (book['title']+' is a '+book['tags'][0]+' book')