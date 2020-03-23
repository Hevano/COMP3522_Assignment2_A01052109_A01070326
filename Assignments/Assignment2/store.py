import order
from order_processor import OrderProcessor
from stock_enum import StockEnum
from inventory import Inventory

class Store:
    def __init__(self):
        self.inventory = Inventory()
        self.logger = None

    def process_orders(self, path):
        op = OrderProcessor(path)
        for o in op.next_order():
            self.inventory.take_order(o)

    def check_inventory(self):
        inv = [item + [StockEnum.INSTOCK] if item[2] > 9 else item for item in self.inventory.check_inventory()]
        inv = [item + [StockEnum.LOW] if 9 >= item[2] > 2 else item for item in inv]
        inv = [item + [StockEnum.VERYLOW] if 2 >= item[2] >= 1 else item for item in inv]
        inv = [item + [StockEnum.VERYLOW] if item[2] <= 0 else item for item in inv]
        return inv
