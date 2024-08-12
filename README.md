# Python Library Inventory Script

## Objective
This task demonstrates basic Python syntax skills by completing a set of three steps to manage a library inventory.

## Deliverable
Create a Python script named `<first_name>_<last_name>.py` and commit it to the branch `feature/<name>-python-1`. Ensure that your implementation covers the three steps outlined below. The code should be well-commented for clarity. Don't forget to create the necessary branch and push your changes to it.

## Steps to Complete

### Step 1: Initialize Book Inventory
1. Create a list named `books` where each element is a dictionary representing a book's information.
2. Each dictionary should contain the following keys:
   - `title`: A string representing the book's title.
   - `author`: A string representing the author's name.
   - `availability`: A boolean indicating if the book is available for checkout.
   - `tags`: A list of strings representing different categories or descriptors of the book.

#### Data to Add:
- **Book 1**: 
  - Title: "Python Fundamentals"
  - Author: "Ahmed Zayed"
  - Availability: `True`
  - Tags: `["Programming", "Python", "Basics"]`
  
- **Book 2**: 
  - Title: "The Art of Coding"
  - Author: "Mohammed Ali"
  - Availability: `False`
  - Tags: `["Coding", "Art", "Creativity"]`
  
- **Book 3**: 
  - Title: "Data Structures in Python"
  - Author: "Yousef Amr"
  - Availability: `True`
  - Tags: `["Data", "Python", "Intermediate"]`

### Step 2: Filter Books by Author and Availability
1. Loop through the `books` list and build a new list named `available_books_by_mohammed`.
2. This list should include titles of books where:
   - The author's name contains "Mohammed".
   - The book's availability is set to `True`.
3. Once compiled, display the contents of `available_books_by_mohammed`.

### Step 3: Analyze Tags with Match Statement
1. For each book in the `books` list, use a `match` statement to check its first tag (`tags[0]`):
   - If the tag is `Programming`, `Coding`, or `Data`, print a message that includes the book's title and a relevant comment about that tag.
   - If none of these tags are present, print the book's title with a message indicating that the tag is unrecognized.

#### Example:
For a book object like:

```python
book = {
    "title": "Data Structures in Python",
    "tags": ["Data", "Algorithms"]
}
```

The output should be:

```
The book "Data Structures in Python" is related to Data.
```
