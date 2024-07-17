# book_class.py

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', publication_year={self.year})"

    def __str__(self):
        return f"'{self.title}' by {self.author} (published in {self.year})"
    
    def __del__(self):
        return f"Deleting({self.year})"
    

    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and 
                    self.author == other.author and 
                    self.year == other.year)
        return False

    def __lt__(self, other):
        if isinstance(other, Book):
            return self.year < other.year
        return NotImplemented

    def __hash__(self):
        return hash((self.title, self.author, self.year))
    
    def delete(self):
        print(f"Deleting {self.title}")

# Example usage
if __name__ == "__main__":
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("Brave New World", "Aldous Huxley", 1932)
    book3 = Book("1984", "George Orwell", 1949)

    print(book1)  # Output: 1984 by George Orwell, published in 1949
    print(repr(book2))  # Output: Book('Brave New World', 'Aldous Huxley', 1932)

    print(book1 == book3)  # Output: True
    print(book1 == book2)  # Output: False

    print(book1 < book2)  # Output: False
    print(book2 < book1)  # Output: True

    books = {book1, book2, book3}
    print(len(books))  # Output: 2, because book1 and book3 are considered the same book

    book1.delete()  # Output: Deleting 1984