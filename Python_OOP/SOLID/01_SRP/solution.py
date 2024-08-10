class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_book(self, title):
        try:
            book = [b for b in self.books if b.title == title][0]
            return book
        except IndexError:
            return "Sorry book is not found"

    def remove_book(self, title):
        for b in self.books:
            if b.title == title:
                del b

