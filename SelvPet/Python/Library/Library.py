class Book:
    """
    Class representing a book in the library.
    """
    def __init__(self, title, author, year, condition="good"):
        self.title = title
        self.author = author
        self.year = year
        self.condition = condition  # "excellent", "good", "poor"
        self.is_available = True
        self.borrowed_by = None

    def get_status(self):
        """Returns a string with full information about the book."""
        status = "available" if self.is_available else "borrowed"
        if not self.is_available:
            status += f" (by {self.borrowed_by})"
        return f"{self.title} ({self.author}, {self.year}) - {status} ({self.condition})"

    def is_available_for_borrow(self):
        """Checks whether the book can be borrowed."""
        return self.is_available and self.condition in ["excellent", "good"]

    def set_condition(self, new_condition):
        """Updates the book condition."""
        self.condition = new_condition
        print(f"The condition of '{self.title}' has been updated to: {new_condition}")


class Reader:
    """
    Class representing a library reader.
    """
    def __init__(self, name, card_number):
        self.name = name
        self.card_number = card_number
        self.borrowed_books = []
        self.has_debts = False

    def get_info(self):
        """Returns information about the reader."""
        books_count = len(self.borrowed_books)
        debt_status = "has debts" if self.has_debts else "no debts"
        books_list = ", ".join([book.title for book in self.borrowed_books]) if self.borrowed_books else "none"
        
        return (f"Reader: {self.name} (card: {self.card_number})\n"
                f"Borrowed books: {books_count}, Debts: {debt_status}\n"
                f"Books: {books_list}")

    def can_borrow_more(self):
        """Checks if the reader can borrow more books."""
        return len(self.borrowed_books) < 3 and not self.has_debts

    def borrow_book(self, book):
        """Attempts to borrow a book."""
        if not self.can_borrow_more():
            return False, "Cannot borrow: limit exceeded or debts exist"
        
        if not book.is_available_for_borrow():
            return False, f"The book '{book.title}' is not available for borrowing"
        
        book.is_available = False
        book.borrowed_by = self.name
        self.borrowed_books.append(book)
        return True, f"The book '{book.title}' was successfully borrowed"

    def return_book(self, book_title):
        """Returns a book."""
        for book in self.borrowed_books:
            if book.title == book_title:
                book.is_available = True
                book.borrowed_by = None
                self.borrowed_books.remove(book)
                return True, f"The book '{book_title}' has been returned"
        return False, f"The book '{book_title}' was not found among borrowed books"

class Library:
    """
    Class representing a library that manages books and readers.
    """
    def __init__(self, name):
        self.name = name
        self.books = []
        self.readers = []

    def add_book(self, book):
        """Adds a book to the library."""
        self.books.append(book)
        print(f"Book '{book.title}' added to the library")

    def add_reader(self, reader):
        """Registers a reader in the library."""
        self.readers.append(reader)
        print(f"Reader {reader.name} registered")

    def find_book(self, title):
        """Finds a book by title."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_reader(self, name):
        """Finds a reader by name."""
        for reader in self.readers:
            if reader.name.lower() == name.lower():
                return reader
        return None

    def borrow_book(self, reader_name, book_title):
        """Main borrowing method."""
        reader = self.find_reader(reader_name)
        book = self.find_book(book_title)
        
        if not reader:
            return f"Error: Reader '{reader_name}' not found"
        
        if not book:
            return f"Error: Book '{book_title}' not found"
        
        success, message = reader.borrow_book(book)
        return message

    def return_book(self, reader_name, book_title):
        """Returns a book."""
        reader = self.find_reader(reader_name)
        if not reader:
            return f"Error: Reader '{reader_name}' not found"
        
        success, message = reader.return_book(book_title)
        return message

    def list_available_books(self):
        """Prints the list of available books."""
        available_books = [book for book in self.books if book.is_available_for_borrow()]
        if not available_books:
            print("No available books")
            return
        
        print("\n=== Available Books ===")
        for book in available_books:
            print(f"- {book.get_status()}")

    def list_all_books(self):
        """Prints all books."""
        print(f"\n=== All Books in '{self.name}' ===")
        for book in self.books:
            print(f"- {book.get_status()}")

    def list_readers(self):
        """Prints all registered readers."""
        print("\n=== Registered Readers ===")
        for reader in self.readers:
            print(reader.get_info())

if __name__ == "__main__":
    # Create library
    city_library = Library("City Library")
    
    # Create books
    book1 = Book("Crime and Punishment", "Fyodor Dostoevsky", 1866, "excellent")
    book2 = Book("War and Peace", "Leo Tolstoy", 1869, "good")
    book3 = Book("Old Book", "Unknown Author", 1800, "poor")
    book4 = Book("The Master and Margarita", "Mikhail Bulgakov", 1967, "excellent")
    
    # Add books
    city_library.add_book(book1)
    city_library.add_book(book2)
    city_library.add_book(book3)
    city_library.add_book(book4)
    
    # Create and register readers
    reader1 = Reader("Ivan Petrov", "R2024001")
    reader2 = Reader("Maria Sidorova", "R2024002")
    
    city_library.add_reader(reader1)
    city_library.add_reader(reader2)
    
    # Initial state
    print("=== INITIAL STATE ===")
    city_library.list_all_books()
    city_library.list_readers()
    
    # Test cases
    print("\n=== SYSTEM TESTING ===")
    
    # Attempt to borrow a book in poor condition
    print("\n1. Attempt to borrow a book in poor condition:")
    result = city_library.borrow_book("Ivan Petrov", "Old Book")
    print(f"Result: {result}")
    
    # Successful borrow
    print("\n2. Successful borrow:")
    result = city_library.borrow_book("Ivan Petrov", "Crime and Punishment")
    print(f"Result: {result}")
    
    # Borrowing already borrowed book
    print("\n3. Attempt to borrow an already borrowed book:")
    result = city_library.borrow_book("Maria Sidorova", "Crime and Punishment")
    print(f"Result: {result}")
    
    # Borrow second book
    print("\n4. Borrowing a second book:")
    result = city_library.borrow_book("Ivan Petrov", "War and Peace")
    print(f"Result: {result}")
    
    # Borrow third book
    print("\n5. Borrowing a third book:")
    result = city_library.borrow_book("Ivan Petrov", "The Master and Margarita")
    print(f"Result: {result}")
    
    # Attempt to borrow fourth book (limit exceeded)
    print("\n6. Attempt to borrow a fourth book:")
    book5 = Book("Eugene Onegin", "Alexander Pushkin", 1833, "excellent")
    city_library.add_book(book5)
    result = city_library.borrow_book("Ivan Petrov", "Eugene Onegin")
    print(f"Result: {result}")
    
    # Current state
    print("\n=== CURRENT STATE ===")
    city_library.list_all_books()
    city_library.list_readers()
    
    # Return book
    print("\n7. Returning a book:")
    result = city_library.return_book("Ivan Petrov", "War and Peace")
    print(f"Result: {result}")
    
    # Another reader borrows returned book
    print("\n8. Borrowing the returned book:")
    result = city_library.borrow_book("Maria Sidorova", "War and Peace")
    print(f"Result: {result}")
    
    # Final state
    print("\n=== FINAL STATE ===")
    city_library.list_all_books()
    city_library.list_readers()
    city_library.list_available_books()
    
    # Testing a reader with debts
    print("\n=== DEBT TEST ===")
    reader3 = Reader("Alex with Debts", "R2024003")
    reader3.has_debts = True
    city_library.add_reader(reader3)
    
    result = city_library.borrow_book("Alex with Debts", "The Master and Margarita")
    print(f"Attempt to borrow with debts: {result}")
