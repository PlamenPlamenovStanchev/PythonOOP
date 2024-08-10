class Book:
    def __int__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


my_book = Book("My book", "Plamen Stanchev", 478)

print(my_book.name)
print(my_book.author)
print(my_book.pages)