from models.cart import Cart
class Customer:
    """Represents a customer with name, contact info, and loyalty status."""

    def __init__(self, name, contact_info, loyalty_member=False):
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_member = loyalty_member
     
        self.cart = Cart()
    
    def apply_discount(self, total):
        """Applies a 10% discount for loyalty members."""
        return total * 0.9 if self.__loyalty_member else total
    
    def set_shopping_cart(self, cart):
        self.shopping_cart = cart
    
    def __str__(self):
        loyalty = "Loyalty Member" if self.__loyalty_member else "Regular Customer"
        return f"{self.__name} - {loyalty}, Contact: {self.__contact_info}"
