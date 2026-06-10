class Book:
    # Class variable to track the total count
    total_books = 0

    def __init__(self, title, author, genre , available = True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available  = available
        # Increase the counter every time __init__ runs
        Book.total_books += 1
    
     # Instruction 1: Create a Book from a dictionary
    @classmethod
    def from_dict(cls, data):
        # Extracts data from dictionary and creates the class instance
        return cls(data["title"], data["author"], data["genre"])
    
    # Instruction 2: Return the total count formatted as requested
    @classmethod
    def get_total(cls):
        return f"Total books registered: {cls.total_books}"
     def borrow(self ):
        if self.available == False :
            raise ValueError ("The book is already borrowed")
        self.available = False 
        print(f"The book {self.title}  is borrowed")

    def return_book(self ):
        if self.available == True :
            raise ValueError ("The book isnot currently borrowed")
        self.available = True  
        print(f"The book {self.title}  is available")
        

    def __str__(self):
        status = "✓" if self.available == True  else "✗"
        return(f"{status} {self.title} | {self.author} |{self.genre} ")
        


b1 = Book("Python Crash Course", "Eric Matthes", "Programming")
b2 = Book("Sapiens", "Yuval Noah Harari", "History")
b3 = Book.from_dict({
    "title": "Deep Work", "author": "Cal Newport", "genre": "Productivity"
})

b1.borrow()
b2.borrow()

print(b1)
print(b2)
print(b3)