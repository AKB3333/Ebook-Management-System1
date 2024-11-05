from models.order_item import OrderItem

class Cart:
    """Class representing a shopping cart."""

    def __init__(self):
        self.items = []

    def add_item(self, ebook, quantity=1):
        """Add an item to the cart or increase its quantity if already present."""
        for item in self.items:
            if item.ebook == ebook:
                item.quantity += quantity
                return
        # If item is not already in the cart, add it
        self.items.append(OrderItem(ebook, quantity))

    def remove_item(self, ebook):
        """Remove an item from the cart."""
        self.items = [item for item in self.items if item.ebook != ebook]

    def get_total_price(self):
        """Calculate the total price of all items in the cart."""
        return sum(item.get_total_price() for item in self.items)

    def clear_cart(self):
        """Empty the cart."""
        self.items.clear()

    def __str__(self):
        return "\n".join(str(item) for item in self.items)