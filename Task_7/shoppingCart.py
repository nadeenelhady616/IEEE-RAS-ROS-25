class ShoppingCart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, item, price):
        if item in self.items:
            self.items[item] += price
        else:
            self.items[item] = price
    
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            print(f"Item '{item}' not found in the cart.")
    
    def calculate_total(self):
        total = sum(self.items.values())
        return total
    
    def display_cart(self):
        if not self.items:
            print("The cart is empty.")
        else:
            print("Current Items in the cart:")
            for item, price in self.items.items():
                print(f"{item} - {price}")
            print(f"Total: {self.calculate_total()}")
