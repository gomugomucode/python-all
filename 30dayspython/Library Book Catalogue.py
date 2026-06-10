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
    
    def __str__(self):
        status = "✓" if self.available else "✗"
        return(f"{status} {self.title} | {self.author} |{self.genre} ")
