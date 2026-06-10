class Book:
    total_books = 0
    def __init__(self , title, author, genre,  available = True):
        self.title  = title
        self.author  = author
        self.genre  = genre
        self.available  = available
        Book.total_books += 1

    