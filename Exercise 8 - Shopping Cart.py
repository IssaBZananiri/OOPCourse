'''
Exercise 8 - Shopping Cart
Author: Issa B. Zananiri
25/11/2023
'''
# Classes: Item, Shopping Cart, Preson
#
class Item:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price
        



class ShoppingCart:
    def __init__(self):
        self.items_in_cart = []
        self.total_price = 0
    
    def add_item(self,new_item):
        self.items_in_cart.append(new_item)

    def remove_item(self, old_item):
        self.items_in_cart.remove(old_item)

    def calculate_total_price(self):
        self.total_price = 0
        for item in self.items_in_cart:
            self.total_price = self.total_price + item.item_price
        
        return self.total_price



item1 = Item("Banana", 15)
item2 = Item("Cucumber", 5)
item3 = Item("Peanuts", 20)

issa_cart = ShoppingCart()
issa_cart.add_item(item1)
issa_cart.add_item(item2)
issa_cart.add_item(item3)

print("The total price of the items in your cart is:  {}".format(issa_cart.calculate_total_price()))
            
issa_cart.remove_item(item3)
print("The total price of the items in your cart is:  {}".format(issa_cart.calculate_total_price()))

