from order import Order
from Item import Item


class Inventory:
    def __init__(self):
        self.items = {}



    def check_inventory(self):
        return [[item.name, item.product_id, item.quantity] for item in self.items.values()]
