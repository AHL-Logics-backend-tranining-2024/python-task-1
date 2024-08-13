books = [ {
    "title": "Python Fundamentals",
    "author": "Ahmed Zayed",
    "availability" : True,
    "tags": ["Programming", "Python", "Basics"]
},
{
    "title": "The Art of Coding",
    "author": "Mohammed Ali",
    "availability" : False,
    "tags": ["Coding", "Art", "Creativity"]
},
{
    "title": "Data Structures in Python",
    "author": "Yousef Amr",
    "availability" : True,
    "tags":["Data", "Python", "Intermediate"]
}
]

# Task one Filter Books by Author and availability
available_books_by_mohammed = []
for book in books:
        if book['author'] == "Mohammed" and book['availability'] == True :
              available_books_by_mohammed.append(book['title'])
      
print("the available books by mohammed are : ", available_books_by_mohammed)


# Task two Analyze Tags with Match Statement
for book in books:
     match book['tags'][0]:
           case "Programming":
                 print("The book " + book['title'] +"is related to Programming")
           case "Coding":
                 print("The book " + book['title'] +"is related to Coding")
           case "Data":
                 print("The book " + book['title'] +"is related to Data")
