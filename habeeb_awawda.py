#initialise a list of dics called books
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
#a list contains availabil books by mohammed
available_books_by_mohammed=[]

#add mohammeds availabil books for the list
for book in books:
    if "Mohammed" in book.get('author') and book.get('availability'):
        available_books_by_mohammed.append(book.get('title'))

#show mohammeds books list
print(available_books_by_mohammed)

#show the recognization status of each book
for book in books:
    match book.get('tags')[0]:
        case 'Programming' | 'Coding' | 'Data':
            print(book.get('title')+', '+'which has been written by '+book.get('author'))
        case _:
            print(book.get('title')+', this tag is unrecognized')


