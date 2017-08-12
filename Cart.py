class Cart:
    def __init__(self):
        self.cart_items = []

    def __add__(self, other):
        self.cart_items.append(other)

    def calculate_total_price(self):
        total_price = 0
        for item in self.cart_items:
            total_price += item.price
        return total_price

