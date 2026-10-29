class Product:
    round_tax = False

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        discounted_price = self.price - (self.price * self.discount_rate)
        print(f"Discounted price for {self.name} ({self.category}): {discounted_price}")
        return discounted_price

    def calculate_tax(self):
        tax = self.price * self.tax_rate
        if self.round_tax:
            tax = round(tax, 2)
        print(f"Tax for {self.name} ({self.category}): {tax}")
        return tax


class Electronics(Product):
    category = "Electronics"
    discount_rate = 0.10
    tax_rate = 0.15

class Clothing(Product):
    category = "Clothing"
    discount_rate = 0.20
    tax_rate = 0.08

class Grocery(Product):
    category = "Grocery"
    discount_rate = 0.05
    tax_rate = 0.02
    round_tax = True
