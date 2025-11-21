import json
from book import Book

class LibraryInventory:
    def __init__(self, filename="books.json"):
        self.books = []
        self.filename = filename
        self.load_from_file()  # Load books from JSON on start

    def add_book(self, title, author, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return False
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_to_file()  # Save after adding
        return True

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def display_all(self):
        if not self.books:
            print("No books in inventory.")
            return
        for book in self.books:
            print(book)

    def save_to_file(self):
        try:
            with open(self.filename, "w") as f:
                json.dump([book.__dict__ for book in self.books], f, indent=4)
        except Exception as e:
            print(f"Error saving books: {e}")

    def load_from_file(self):
        try:
            with open(self.filename, "r") as f:
                books_data = json.load(f)
                self.books = [Book(**data) for data in books_data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []
