# main.py

from book_class import Book

def main():
    # Creating an instance of Book
    book1 = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method
    print(book1)  # Expected to use __str__

    # Demonstrating the __repr__ method
    print(repr(book1))  # Expected to use __repr__

    # Deleting a book instance to trigger __del__
    del book1

if __name__ == "__main__":
    main()
