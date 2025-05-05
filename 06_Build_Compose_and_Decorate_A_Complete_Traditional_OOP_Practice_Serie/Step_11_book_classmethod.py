class Book:
    total_books = 0  # Class variable

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage
book1 = Book("Python Basics")
book2 = Book("OOP in Python")
book3 = Book("Data Structures")

print("Total Books:", Book.total_books)
