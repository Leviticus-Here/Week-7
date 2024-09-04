# source.py
from book import Book
from library import Library

# Create some book objects
book1 = Book("True Marksmanship", "John Marston")
book2 = Book("Survival 101", "Bear Grylls")
book3 = Book("Rough Rider", "Teddy Roosevelt")

# Create a library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Borrow and return books
print(library.borrow_book("True Marksmanship")) # Borrow book1
print(library.borrow_book("True Marksmanship")) # Already borrowed
print(library.return_book("True Marksmanship")) # Return book1
print(library.return_book("True Marksmanship")) # Not already borrowed

# Count how many books are currently borrowed
print(f"You have borrowed {library.borrowed_count} books from the library.")