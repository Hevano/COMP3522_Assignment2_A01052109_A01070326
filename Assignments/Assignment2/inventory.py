from order import Order


class Inventory:
    def __init__(self):
        self.items = {}

    def take_order(self, order):
        if order.product_id not in self.items:
            print(f"Taking order: {order.orderNo} | {order.name}")
            factory = order.factory()
            product = factory.create(order)
            product.quantity = 100
            self.items[product.product_id] = product
        elif self.items[order.product_id].quantity < order.quantity:
            self.items[order.product_id].quantity += 100

        self.items[order.product_id] -= order.quantity

    def check_inventory(self):
        return [[item.name, item.product_id, item.quantity] for item in self.items.values()]
