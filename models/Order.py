from .order_item import OrderItem

class Order:
    """Represents an order with a list of items."""

    def __init__(self, customer,cart):
        self.__customer = customer
        self.__items = []
        self.items = cart.items
        
    def get_total_price(self):
        """Calculate the total price for the order."""
        return sum(item.get_total_price() for item in self.items)

    def generate_invoice(self):
        """Generate an invoice for this order."""
        invoice = Invoice(self.customer, self)
        return invoice

    def __str__(self):
        return "\n".join(str(item) for item in self.items)