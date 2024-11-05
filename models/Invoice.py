from .order import Order

class Invoice:
    """Represents an invoice generated for a completed order."""

    def __init__(self, order):
        self.__order = order
        self.__vat_rate = 0.08  # 8% VAT

    def calculate_subtotal(self):
        return sum(item.total_price() for item in self.__order.items)

    def calculate_discount(self):
        """Applies a 20% discount for bulk purchases (5 or more items)."""
        if len(self.__order.items) >= 5:
            return self.calculate_subtotal() * 0.2  # 20% discount for bulk purchase
        return 0

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        total_after_discount = subtotal - discount
        vat = total_after_discount * self.__vat_rate
        return total_after_discount + vat

    def generate_invoice(self):
        """Generates a detailed invoice as a string."""
        invoice_details = f"Invoice for {self.__order.customer}\nItems:\n"
        for item in self.__order.items:
            invoice_details += f"{item}\n"
        
        invoice_details += f"\nSubtotal: {self.calculate_subtotal():.2f}"
        invoice_details += f"\nDiscount: -{self.calculate_discount():.2f}"
        invoice_details += f"\nVAT (8%): +{self.calculate_total() - (self.calculate_subtotal() - self.calculate_discount()):.2f}"
        invoice_details += f"\nTotal: {self.calculate_total():.2f}"
        
        return invoice_details

    def __str__(self):
        return self.generate_invoice()
