import order
from order_processor import OrderProcessor
from stock_enum import StockEnum
from datetime import datetime
from inventory import Inventory


class Store:
    exception_message = ""

    def __init__(self):
        self.inventory = Inventory()
        self.logger = None


    def take_order(self, order):
        if order.product_id not in self.inventory.items.keys():
            factory = order.factory()
            product = factory.create(order)

            # if type(product) is str:
            #     Store.exception_message = product
            #     return

            product.quantity = 100
            self.inventory.items[order.product_id] = product
        elif self.inventory.items[order.product_id1].quantity < order.quantity:
            self.inventory.items[order.product_id].quantity += 100

        self.inventory.items[order.product_id].quantity -= order.quantity

    def process_orders(self, path):
        op = OrderProcessor(path)
        text_name = self.create_transaction()

        for o in op.next_order():
            self.take_order(o)
            self.add_transaction(o, text_name)
            Store.exception_message = ""

    def check_inventory(self):
        inv = [item + [StockEnum.INSTOCK] if item[2] > 9 else item for item in self.inventory.check_inventory()]
        inv = [item + [StockEnum.LOW] if 9 >= item[2] > 2 else item for item in inv]
        inv = [item + [StockEnum.VERYLOW] if 2 >= item[2] >= 1 else item for item in inv]
        inv = [item + [StockEnum.VERYLOW] if item[2] <= 0 else item for item in inv]
        return inv

    def create_transaction(self):
        # datetime object containing current date and time
        now = datetime.now()

        # dd-mm-YY H:M
        dt_string = now.strftime("%d-%m-%Y %H:%M")
        text_file_name = now.strftime("DTR_%d%m%Y_%H%M")
        with open(text_file_name, encoding="utf-8", mode="w") as text_file:
            text_file.write("HOLIDAY STORE - DAILY TRANSACTION REPORT (DRT)\n %s" % dt_string)

        return text_file_name

    def add_transaction(self, o, text_name):
        with open(text_name, encoding="utf-8", mode="a") as text_file:

            if not o.details['corrupted']:
                text_file.write(
                    f'\n{o.orderNo} Item {o.name}, Product ID {o.product_id}, Name {o.name}, Quantity {o.quantity}')
            else:
                text_file.write(f"\nOrder {o.orderNo}, Could not process order data was corrupted, InvalidDataError -"
                                f"{o.details['error']}")

