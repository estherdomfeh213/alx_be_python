class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = False  

  def check_out(self):
    self._is_checked_out = True

  def return_book(self):
    self._is_checked_out = False

  def is_available(self):
    return not self._is_checked_out


class Library:
  def __init__(self):
    self._books = []

  def add_book(self, book):
    self._books.append(book)

  def check_out_book(self, title):
    for book in self._books:
      if book.title == title and book.is_available():
        book.check_out()
        print(f"'{title}' has been checked out.")
        return
      print(f"'{title}' is unavailable.")

  def return_book(self, title):
    for book in self._books:
      if book.title == title and not book.is_available():
        book.return_book()
        print(f"'{title}' has been returned.")
        return
      print(f"'{title}' is not checked out.")

  def list_available_books(self):
    for book in self._books:
      if book.is_available():
        print(f"{book.title} by {book.author}")
        if not any(book.is_available() for book in self._books):
          print("No available books at the moment.")
