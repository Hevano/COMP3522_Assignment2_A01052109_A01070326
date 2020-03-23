import abc


class Item(abc.ABC):

    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name
        self.quantity = 0


