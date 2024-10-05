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