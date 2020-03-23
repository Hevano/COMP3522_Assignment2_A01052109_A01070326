from order import Order


class Inventory:
    def __init__(self):
        self.items = {}

    def take_order(self, order):
        if order.product_id not in self.items:
            factory = order.factory()
            factory.create(order)
        elif self.items[order.product_id].quantity < order.quantity:
            self.items[order.product_id].quantity += 100

        self.items[order.product_id] -= order.quantity

    def check_inventory(self):
        return [[item.name, item.product_id, item.quantity] for item in self.items.values()]
