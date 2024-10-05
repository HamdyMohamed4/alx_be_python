class Book:
  """
  Represents a book with title, author, and availability status.
  """

  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = False  # Private attribute for availability

  def check_out(self):
    """Marks the book as checked out (unavailable)."""
    self._is_checked_out = True

  def return_book(self):
    """Marks the book as returned (available)."""
    self._is_checked_out = False

  def is_available(self):
    """Returns True if the book is available, False otherwise."""
    return not self._is_checked_out

  def __str__(self):
    """Provides a string representation of the book."""
    return f"{self.title} by {self.author}"
    
class Library:
  """
  Represents a library with a collection of books and management methods.
  """

  def __init__(self):
    self._books = []  # Private list to store Book instances

  def add_book(self, book):
    """Adds a Book object to the library's collection."""
    self._books.append(book)

  def check_out_book(self, title):
    """Attempts to check out a book by title, marking it unavailable."""
    for book in self._books:
      if book.title == title and book.is_available():
        book.check_out()
        print(f"Successfully checked out '{title}'.")
        return
    print(f"Sorry, '{title}' is not available or does not exist.")

  def return_book(self, title):
    """Attempts to return a book by title, marking it available."""
    for book in self._books:
      if book.title == title:
        book.return_book()
        print(f"Successfully returned '{title}'.")
        return
    print(f"Sorry, '{title}' is not currently checked out.")

  def list_available_books(self):
    """Prints all books in the library that are currently available."""
    print("Available books:")
    for book in self._books:
      if book.is_available():
        print(book)

# You can import Book and Library from this file in your main.py