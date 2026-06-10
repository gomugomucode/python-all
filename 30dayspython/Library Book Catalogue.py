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