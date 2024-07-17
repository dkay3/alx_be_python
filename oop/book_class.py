# book_class.py

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', publication_year={self.publication_year})"

    def __str__(self):
        return f"'{self.title}' by {self.author} (published in {self.publication_year})"
    

    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and 
                    self.author == other.author and 
                    self.publication_year == other.publication_year)
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.publication_year < other.publication_year
        return NotImplemented

    def __hash__(self):
        return hash((self.title, self.author, self.publication_year))

# Example usage
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("Brave New World", "Aldous Huxley", 1932)
    book3 = Book("1984", "George Orwell", 1949)

    print(book1)  # Output: '1984' by George Orwell (published in 1949)
    print(repr(book2))  # Output: Book(title='Brave New World', author='Aldous Huxley', publication_year=1932)

    print(book1 == book3)  # Output: True
    print(book1 == book2)  # Output: False

    print(book1 < book2)  # Output: False
    print(book2 < book1)  # Output: True

    books = {book1, book2, book3}
    print(len(books))  # Output: 2, because book1 and book3 are considered the same book
