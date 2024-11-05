from .ebook import EBook

class Catalog:
    """Manages the collection of e-books in the store."""

    def __init__(self):
        self.__ebooks = []

    def add_ebook(self, ebook):
        self.__ebooks.append(ebook)

    def remove_ebook(self, ebook_title):
        self.__ebooks = [book for book in self.__ebooks if book.title != ebook_title]

    def list_ebooks(self):
        return self.__ebooks

    def __str__(self):
        return "\n".join(str(ebook) for ebook in self.__ebooks)
