from models.order_item import OrderItem

class ShoppingCart:
    """Class representing a shopping cart for a customer."""

    def __init__(self):
        self.items = []

    def add_item(self, ebook, quantity=1):
        order_item = OrderItem(ebook, quantity)
        self.items.append(order_item)

    def remove_item(self, ebook):
        self.items = [item for item in self.items if item.ebook != ebook]

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items)

    def __str__(self):
        return "\n".join(str(item) for item in self.items)