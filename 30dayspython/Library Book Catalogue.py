class Book:
    # Class variable to track the total count
    total_books = 0

    def __init__(self, title, author, genre, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
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

    def borrow(self):
        try:
            if self.available == False:
                raise ValueError(f"'{self.title}' is already borrowed")
            self.available = False
        except ValueError as e:
            print(f"❌ ValueError: {e}")

    def return_book(self):
        try:
            if self.available == True:
                raise ValueError(f"'{self.title}' is not currently borrowed")
            self.available = True  
        except ValueError as e:
            print(f"[✗] ValueError: {e}") 

    def __str__(self):
        status = "✓" if self.available == True else "✗"
        return f"[{status}] {self.title} | {self.author} | {self.genre}"


# --- TASK 4 TESTING EXECUTION ---

# 1. Create 4 books (including one via from_dict)
b1 = Book("Python Crash Course", "Eric Matthes", "Programming")
b2 = Book("Sapiens", "Yuval Noah Harari", "History")
b3 = Book.from_dict({
    "title": "Deep Work", "author": "Cal Newport", "genre": "Productivity"
})
b4 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy") 

# 2. Borrow 2 books
b1.borrow()
b2.borrow()

# 3. Print all books
print(b1)
print(b2)
print(b3)
print(b4)

# 4. Return one book and print it again
b1.return_book()
print(b1) 

# 5. Try to borrow the same book again and handle the exception
b2.borrow()


# 6. Print the total count
print(Book.get_total())
