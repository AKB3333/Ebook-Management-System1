from models.ebook import Ebook
from models.catalog import Catalog
from models.customer import Customer
from models.shopping_cart import ShoppingCart
from models.order import Order
from models.order_item import OrderItem

def test_ebookstore():
    # Create e-books
    ebook1 = Ebook("Python 101", "John Doe", "2022-01-01", "Programming", 15.99)
    ebook2 = Ebook("Advanced Python", "Jane Smith", "2023-01-01", "Programming", 25.99)

    # Add to catalog
    catalog = Catalog()
    catalog.add_ebook(ebook1)
    catalog.add_ebook(ebook2)

    # Create a customer
    customer = Customer("Alice", "alice@example.com", is_loyalty_member=True)

    # Create shopping cart
    customer.cart.add_item(ebook1, 3)
    customer.cart.add_item(ebook2, 2)

    # Create an order
    order = Order(customer)
    for item in cart.items:
        order.add_item(item)

    # Generate invoice
    invoice = order.generate_invoice()
    print(invoice)

if __name__ == "__main__":
    test_ebookstore()