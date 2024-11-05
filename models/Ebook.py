class EBook:
    """Represents an e-book with details like title, author, and price."""

    def __init__(self, title, author, publication_date, genre, price):
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    @property
    def title(self):
        return self.__title

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"{self.__title} by {self.__author} - {self.__genre}, Price: {self.__price}"
