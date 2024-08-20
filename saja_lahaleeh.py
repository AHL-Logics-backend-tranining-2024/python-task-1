
#T1 :Create a list consisting of dictionary 
books=[
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
        "Availability" : True,
        "Tags":["Data", "Python", "Intermediate"]
    }

]
#T2 :Filter Books according to the Author
available_books_by_mohammed=[]

for book in books:
    if "Mohammed" in book["Author"] and book['Availability']==True:
        available_books_by_mohammed.append(book['Title'])

print(available_books_by_mohammed)

#T3 :Analyze Tags with Match Statement

for book in books:
     match book['Tags'][0]:
           case "Programming":
                 print("The book " + book['Title'] +" is related to Programming")
           case "Coding":
                 print("The book " + book['Title'] +" is related to Coding")
           case "Data":
                 print("The book " + book['Title'] +" is related to Data")
           case _:
                 print("The book " + book['Title'] + " has no tag")
   

      