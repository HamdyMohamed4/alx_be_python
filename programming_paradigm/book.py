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