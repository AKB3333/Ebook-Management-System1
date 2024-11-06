from models.ebook import Ebook
from models.catalog import Catalog
from models.customer import Customer
from models.shopping_cart import ShoppingCart
from models.order import Order


def main():
    # Initialize catalog, customer, cart, and order for demonstration
    catalog = Catalog()
    ebook1 = Ebook("Learn Python", "Author A", "2022-02-22", "Education", 12.99)
    catalog.add_ebook(ebook1)

    customer = Customer("John Doe", "john@example.com", is_loyalty_member=True)
    cart = ShoppingCart()
    cart.add_item(ebook1, 5)

    customer.set_shopping_cart(cart)
    order = Order(customer)
    for item in cart.items:
        order.add_item(item)

    invoice = order.generate_invoice()
    print(invoice)

if __name__ == "__main__":
    main()
