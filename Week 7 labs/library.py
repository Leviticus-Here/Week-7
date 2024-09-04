# library.py
class Library:
    def __init__(self):
        self.books = []
        self.borrowed_count = 0
    def add_book(self, book):
        self.books.append(book)
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.borrow():
                    self.borrowed_count += 1
                    return f"You have successfully borrowed: {title}"
                else:
                    return f"Apologies. {title} is already being borrowed"
        return f"Error 404 {title} is not found in library"
    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.return_book():
                    self.borrowed_count -= 1
                    return f"You have successfully returned: {title}"
                else:
                    return f"Apologies. {title} is not already borrowed"
        return f"Error 404 {title} is not found in library"