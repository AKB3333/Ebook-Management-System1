class OrderItem:
    """Represents a single item in an order."""

    def __init__(self, ebook, quantity=1):
        self.__ebook = ebook
        self.__quantity = quantity

    def total_price(self):
        return self.__ebook.price * self.__quantity

    def __str__(self):
        return f"{self.__ebook.title} - {self.__quantity} x {self.__ebook.price} = {self.total_price()}"
