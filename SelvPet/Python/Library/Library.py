# ====== КЛАСС КНИГИ ======
class Book:
    """
    Класс для представления книги в библиотеке.
    """
    def __init__(self, title, author, year, condition="хорошее"):
        self.title = title
        self.author = author
        self.year = year
        self.condition = condition  # "отличное", "хорошее", "плохое"
        self.is_available = True
        self.borrowed_by = None

    def get_status(self):
        """Возвращает строку с полной информацией о книге."""
        status = "доступна" if self.is_available else "выдана"
        if not self.is_available:
            status += f" ({self.borrowed_by})"
        return f"{self.title} ({self.author}, {self.year}) - {status} ({self.condition})"

    def is_available_for_borrow(self):
        """Проверяет, доступна ли книга для выдачи."""
        return self.is_available and self.condition in ["отличное", "хорошее"]

    def set_condition(self, new_condition):
        """Изменяет состояние книги."""
        self.condition = new_condition
        print(f"Состояние книги '{self.title}' изменено на: {new_condition}")

# ====== КЛАСС ЧИТАТЕЛЯ ======
class Reader:
    """
    Класс для представления читателя библиотеки.
    """
    def __init__(self, name, card_number):
        self.name = name
        self.card_number = card_number
        self.borrowed_books = []
        self.has_debts = False

    def get_info(self):
        """Возвращает информацию о читателе."""
        books_count = len(self.borrowed_books)
        debt_status = "есть долги" if self.has_debts else "нет долгов"
        books_list = ", ".join([book.title for book in self.borrowed_books]) if self.borrowed_books else "нет"
        
        return f"Читатель: {self.name} (билет: {self.card_number})\n" \
               f"Взято книг: {books_count}, Долги: {debt_status}\n" \
               f"Книги: {books_list}"

    def can_borrow_more(self):
        """Проверяет, может ли читатель взять еще книги."""
        return len(self.borrowed_books) < 3 and not self.has_debts

    def borrow_book(self, book):
        """Метод для взятия книги."""
        if not self.can_borrow_more():
            return False, "Не может взять книгу: превышен лимит или есть долги"
        
        if not book.is_available_for_borrow():
            return False, f"Книга '{book.title}' недоступна для выдачи"
        
        book.is_available = False
        book.borrowed_by = self.name
        self.borrowed_books.append(book)
        return True, f"Книга '{book.title}' успешно выдана"

    def return_book(self, book_title):
        """Метод для возврата книги."""
        for book in self.borrowed_books:
            if book.title == book_title:
                book.is_available = True
                book.borrowed_by = None
                self.borrowed_books.remove(book)
                return True, f"Книга '{book_title}' возвращена"
        return False, f"Книга '{book_title}' не найдена у читателя"

# ====== КЛАСС БИБЛИОТЕКИ ======
class Library:
    """
    Класс, представляющий библиотеку и управляющий книгами и читателями.
    """
    def __init__(self, name):
        self.name = name
        self.books = []
        self.readers = []

    def add_book(self, book):
        """Добавляет книгу в библиотеку."""
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку")

    def add_reader(self, reader):
        """Регистрирует читателя в библиотеке."""
        self.readers.append(reader)
        print(f"Читатель {reader.name} зарегистрирован")

    def find_book(self, title):
        """Находит книгу по названию."""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_reader(self, name):
        """Находит читателя по имени."""
        for reader in self.readers:
            if reader.name.lower() == name.lower():
                return reader
        return None

    def borrow_book(self, reader_name, book_title):
        """Основной метод выдачи книги."""
        reader = self.find_reader(reader_name)
        book = self.find_book(book_title)
        
        if not reader:
            return f"Ошибка: Читатель '{reader_name}' не найден"
        
        if not book:
            return f"Ошибка: Книга '{book_title}' не найдена"
        
        success, message = reader.borrow_book(book)
        return message

    def return_book(self, reader_name, book_title):
        """Метод для возврата книги."""
        reader = self.find_reader(reader_name)
        if not reader:
            return f"Ошибка: Читатель '{reader_name}' не найден"
        
        success, message = reader.return_book(book_title)
        return message

    def list_available_books(self):
        """Выводит список доступных книг."""
        available_books = [book for book in self.books if book.is_available_for_borrow()]
        if not available_books:
            print("Нет доступных книг")
            return
        
        print("\n=== Доступные книги ===")
        for book in available_books:
            print(f"- {book.get_status()}")

    def list_all_books(self):
        """Выводит список всех книг."""
        print(f"\n=== Все книги библиотеки '{self.name}' ===")
        for book in self.books:
            print(f"- {book.get_status()}")

    def list_readers(self):
        """Выводит список всех читателей."""
        print(f"\n=== Зарегистрированные читатели ===")
        for reader in self.readers:
            print(reader.get_info())

# ====== ТОЧКА ВХОДА (ОСНОВНАЯ ЛОГИКА ПРОГРАММЫ) ======
if __name__ == "__main__":
    # Создаем библиотеку
    city_library = Library("Городская библиотека")
    
    # Создаем книги
    book1 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, "отличное")
    book2 = Book("Война и мир", "Лев Толстой", 1869, "хорошее")
    book3 = Book("Старая книга", "Неизвестный автор", 1800, "плохое")
    book4 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "отличное")
    
    # Добавляем книги в библиотеку
    city_library.add_book(book1)
    city_library.add_book(book2)
    city_library.add_book(book3)
    city_library.add_book(book4)
    
    # Создаем и регистрируем читателей
    reader1 = Reader("Иван Петров", "Ч2024001")
    reader2 = Reader("Мария Сидорова", "Ч2024002")
    
    city_library.add_reader(reader1)
    city_library.add_reader(reader2)
    
    # Показываем начальное состояние
    print("=== НАЧАЛЬНОЕ СОСТОЯНИЕ ===")
    city_library.list_all_books()
    city_library.list_readers()
    
    # Тестируем различные сценарии
    print("\n=== ТЕСТИРОВАНИЕ СИСТЕМЫ ===")
    
    # Попытка взять книгу в плохом состоянии
    print("\n1. Попытка взять книгу в плохом состоянии:")
    result = city_library.borrow_book("Иван Петров", "Старая книга")
    print(f"Результат: {result}")
    
    # Успешное взятие книги
    print("\n2. Успешное взятие книги:")
    result = city_library.borrow_book("Иван Петров", "Преступление и наказание")
    print(f"Результат: {result}")
    
    # Попытка взять уже взятую книгу
    print("\n3. Попытка взять уже взятую книгу:")
    result = city_library.borrow_book("Мария Сидорова", "Преступление и наказание")
    print(f"Результат: {result}")
    
    # Взятие второй книги
    print("\n4. Взятие второй книги:")
    result = city_library.borrow_book("Иван Петров", "Война и мир")
    print(f"Результат: {result}")
    
    # Взятие третьей книги
    print("\n5. Взятие третьей книги:")
    result = city_library.borrow_book("Иван Петров", "Мастер и Маргарита")
    print(f"Результат: {result}")
    
    # Попытка взять четвертую книгу (превышение лимита)
    print("\n6. Попытка взять четвертую книгу:")
    book5 = Book("Евгений Онегин", "Александр Пушкин", 1833, "отличное")
    city_library.add_book(book5)
    result = city_library.borrow_book("Иван Петров", "Евгений Онегин")
    print(f"Результат: {result}")
    
    # Показываем текущее состояние
    print("\n=== ТЕКУЩЕЕ СОСТОЯНИЕ ===")
    city_library.list_all_books()
    city_library.list_readers()
    
    # Возврат книги
    print("\n7. Возврат книги:")
    result = city_library.return_book("Иван Петров", "Война и мир")
    print(f"Результат: {result}")
    
    # Попытка другого читателя взять возвращенную книгу
    print("\n8. Попытка взять возвращенную книгу:")
    result = city_library.borrow_book("Мария Сидорова", "Война и мир")
    print(f"Результат: {result}")
    
    # Финальное состояние
    print("\n=== ФИНАЛЬНОЕ СОСТОЯНИЕ ===")
    city_library.list_all_books()
    city_library.list_readers()
    city_library.list_available_books()
    
    # Тестирование читателя с долгами
    print("\n=== ТЕСТ С ДОЛГАМИ ===")
    reader3 = Reader("Алексей с долгами", "Ч2024003")
    reader3.has_debts = True
    city_library.add_reader(reader3)
    
    result = city_library.borrow_book("Алексей с долгами", "Мастер и Маргарита")
    print(f"Попытка взять книгу с долгами: {result}")

       
   
