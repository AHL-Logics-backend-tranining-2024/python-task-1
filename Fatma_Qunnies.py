#list ,Create a list consisting of dictionary 
books = [
    {"title": "Python Fundamentals",#dict have key and value
        "author": "Ahmed Zayed",
        "availability": True,
        "tags":["Programming", "Python", "Basics"]#dictionary have a list of tags
        },
    {
        "title":"The Art of Coding",
        "author":"Mohammed Ali",
        "availability": False,
        "tags": ["Coding", "Art","Creativity"]
    },{
        "title":"Data Structures in Python",
        "author":"Yousef Amr",
        "availability": True,
        "tags": ["Data","Python","Intermediate"]}]
# Step 2: Filter Books by Author
available_books_by_mohammed = []
for book in books:
     if "Mohammed" in book["author"] and book["availability"]:
        available_books_by_mohammed.append(book["title"])
        # print(book["availability"])

# print 
print(available_books_by_mohammed)


# Step 3: Analyze Tags with Match Statement

def matchs(book):
  s = book["tags"][0]
  match s:
        case "Programming" |"Coding" |"Data":
            return "The book \""+ book['title'] +"\"is related to "+ book['tags'][0]
        case _:
            return "The book \""+ book['title'] +"\" has an unrecognized tag."
            
   

for book in books :
   print (matchs(book))
