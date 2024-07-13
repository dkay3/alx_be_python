class Book:
    """A class representing a book with a title, author, and availability status."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Marks the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Checks if the book is available."""
        return not self._is_checked_out

    def __repr__(self):
        """String representation of the book."""
        status = "Available" if self.is_available() else "Checked Out"
        return f"'{self.title}' by {self.author} ({status})"


class Library:
    """A class representing a library containing a collection of books."""

    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        """Returns a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        """Lists all available books in the library."""
        return [book for book in self._books if book.is_available()]

# Example usage:
if __name__ == "__main__":
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    print("Available books:")
    print(library.list_available_books())

    library.check_out_book("1984")
    print("\nChecked out '1984'")

    print("\nAvailable books after checking out '1984':")
    print(library.list_available_books())

    library.return_book("1984")
    print("\nReturned '1984'")

    print("\nAvailable books after returning '1984':")
    print(library.list_available_books())
