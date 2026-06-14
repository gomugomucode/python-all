from functools import wraps
from typing import Generator, Iterator, List, Optional


# ==========================================
# DECORATORS (Stretch Goal)
# ==========================================
def log_action(func):
    """Decorator to log borrow and return operations."""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        action = func.__name__.replace("_", " ").capitalize()
        print(f"[LOG] {action} processed for: '{self.title}' (ISBN: {self.isbn})")
        return result
    return wrapper


# ==========================================
# BASE CLASS
# ==========================================
class Book:
    """Represents a standard physical book."""
    
    def __init__(self, title: str, author: str, isbn: str) -> None:
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn
        # Encapsulation: Private attribute to manage borrow state
        self.__is_borrowed: bool = False

    # Encapsulation / Stretch Goal: Property for clean read-only availability
    @property
    def is_available(self) -> bool:
        """Returns True if the book is available, False if borrowed."""
        return not self.__is_borrowed

    # Encapsulation: State modifications restricted to these methods
    @log_action
    def borrow(self) -> bool:
        """Borrows the book if it is available."""
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        print(f"Error: '{self.title}' is already borrowed.")
        return False

    @log_action
    def return_book(self) -> bool:
        """Returns the borrowed book."""
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        print(f"Error: '{self.title}' was not borrowed.")
        return False

    # Polymorphism: Target for overriding in child classes
    def display_info(self) -> str:
        """Returns a formatted string of core book information."""
        status = "Available" if self.is_available else "Borrowed"
        return f"[Physical Book] {self.title} by {self.author} (ISBN: {self.isbn}) - Status: {status}"

    # Dunder Methods
    def __str__(self) -> str:
        return f"'{self.title}' by {self.author}"

    def __repr__(self) -> str:
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn


# ==========================================
# INHERITED SUBCLASSES
# ==========================================
class EBook(Book):
    """Represents an electronic book with file size metadata."""
    
    def __init__(self, title: str, author: str, isbn: str, file_size_mb: float) -> None:
        # Inheritance: Reusing base initialization via super()
        super().__init__(title, author, isbn)
        self.file_size_mb: float = file_size_mb

    # Polymorphism: Overriding display info for EBooks
    def display_info(self) -> str:
        status = "Available" if self.is_available else "Borrowed"
        return f"[E-Book] {self.title} by {self.author} (ISBN: {self.isbn}) [{self.file_size_mb} MB] - Status: {status}"

    def __repr__(self) -> str:
        return f"EBook(title='{self.title}', author='{self.author}', isbn='{self.isbn}', file_size_mb={self.file_size_mb})"


class AudioBook(Book):
    """Represents an audiobook with duration and narrator metadata."""
    
    def __init__(self, title: str, author: str, isbn: str, duration_hours: float, narrator: str) -> None:
        # Inheritance: Reusing base initialization via super()
        super().__init__(title, author, isbn)
        self.duration_hours: float = duration_hours
        self.narrator: str = narrator

    # Polymorphism: Overriding display info for AudioBooks
    def display_info(self) -> str:
        status = "Available" if self.is_available else "Borrowed"
        return f"[Audiobook] {self.title} by {self.author} (ISBN: {self.isbn}) [Narrated by: {self.narrator}, {self.duration_hours} hrs] - Status: {status}"

    def __repr__(self) -> str:
        return f"AudioBook(title='{self.title}', author='{self.author}', isbn='{self.isbn}', duration_hours={self.duration_hours}, narrator='{self.narrator}')"


# ==========================================
# COMPOSITION CONTAINER CLASS
# ==========================================
class Library:
    """Manages a collection of books using composition."""
    
    def __init__(self, name: str) -> None:
        self.name: str = name
        # Composition: Library "has-a" list of Book items
        self.__books: List[Book] = []

    def add(self, book: Book) -> None:
        """Adds a book to the library catalog."""
        if book not in self.__books:
            self.__books.append(book)
        else:
            print(f"Book with ISBN {book.isbn} already exists in the library.")

    # Stretch Goal: Generator to yield only currently available items
    def available_books(self) -> Generator[Book, None, None]:
        """Yields books that are currently available for borrowing."""
        for book in self.__books:
            if book.is_available:
                yield book

    # Dunder Methods
    def __len__(self) -> int:
        return len(self.__books)

    def __getitem__(self, index: int) -> Book:
        return self.__books[index]

    def __iter__(self) -> Iterator[Book]:
        return iter(self.__books)

    def __contains__(self, item: object) -> bool:
        if isinstance(item, Book):
            return item in self.__books
        elif isinstance(item, str):
            # Fallback functionality: check presence by matching ISBN string
            return any(book.isbn == item for book in self.__books)
        return False


# 1. Initialization and Composition
lib = Library("Dlytica Library")
lib.add(Book("Atomic Habits", "Clear", "111"))
lib.add(EBook("Deep Learning", "Goodfellow", "222", file_size_mb=25))
lib.add(AudioBook("Sapiens", "Harari", "333", duration_hours=15, narrator="Perkins"))

print("--- Testing __len__ ---")
print(len(lib))  # Expected Output: 3

print("\n--- Testing __getitem__ and __str__ ---")
print(lib[0])    # Expected Output: 'Atomic Habits' by Clear

print("\n--- Testing Iteration and Polymorphism ---")
for item in lib:
    print(item.display_info())
    # Expected: Prints separate unique formats for physical, e-book, and audiobook

print("\n--- Testing Encapsulation and Decorators ---")
lib[1].borrow()  # Expected: Logs the borrow action safely

print("\n--- Testing Stretch Properties ---")
print(lib[1].is_available)  # Expected Output: False
