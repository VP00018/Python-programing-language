# Magic Method = Dunder Method (DoubleUnderscore) __init__, __str__, __eq__
# they are automatically called by many of python's built-in operations.
# They allow developer to define or customize the behaviour of object.

class Book:
    def __init__ (self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other): # less than
        return self.num_pages < other.num_pages
    
    def __gt__(self, other): # greater than
        return self.num_pages > other.num_pages
    
    def __add__(self, other): # ADD BOTH PAGES
        return f"{self.num_pages + other.num_pages} pages "

book1 = Book("The Hobbit", "J.R.R. Tolkien", 320)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.k.Rowling", 223)
book3 = Book("The Lion, the Witch and the wardrobe", "C.S. Lewis", 410)

# print(book3)
# print(book1 == book3)

print(book2 + book3)
