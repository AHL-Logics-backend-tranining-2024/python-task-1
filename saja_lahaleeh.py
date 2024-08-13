
#T1
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
#T2
available_books_by_mohammed=[]

for book in books:
    if "Mohammed" in book["Author"] and book['Availability']==True:
        available_books_by_mohammed.append(book['Title'])

print(available_books_by_mohammed)

#T3

for book in books:
    for tag in book["Tags"]:
        if tag=="Data" or tag=="Programming" or tag=="Coding":
            print ("The book ",book['Title']," is related to ",tag,".")