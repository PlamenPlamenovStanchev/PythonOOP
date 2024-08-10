from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book):
        pass


class PaperFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:3]


class InstagramFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content


class FacebookFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:20]


class TicTokFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return f"@@ {book.content} ##"


class Printer:
    def get_book(self, book: Book, formatter: BaseFormatter):
        formatted_book = formatter.format(book)
        return formatted_book
