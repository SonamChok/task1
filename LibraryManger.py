# Initialize empty lists,sets, and dictonary
books_list = []
authors_set = set()
books_dict={}

#add books
books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"]="John Smth"

books_list.append("Data Structures and Alogorithms")
authors_set.add("Jane Doe")
books_dict["Data Structures and Algorithms"]="Jane Doe"

books_list.append("Machine Learning Basics")
authors_set.add("Alice Johson")
books_dict["Machine Learning Basics"]="Alice Johson"

# Search for  book
search_title=input ("Ener the title of the book to search:")
if search_title in books_list:
    print(f"Book found! Author:{books_dict[search_title]}")
else:
    print("Books not found!")
    
#Display all books
print("Lst of Books:")
for book in books_list:
    print(book)
    
#remove a book 
remove_title=input("Enter the title of the book to remove or else enter to skp:")
if remove_title in books_list:
    remove_author=books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Book removed successflly!")
    print("Books available:", books_list)
    
else:
    print("Book not found!")
    
    
    
    
    
    
