from shoppingCart import ShoppingCart

cart = ShoppingCart()
cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("orange", 150)

cart.display_cart()
cart.remove_item("orange")
cart.display_cart()