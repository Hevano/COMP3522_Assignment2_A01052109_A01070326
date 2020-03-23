import abc
from Item import Item


class Toy(Item, abc.ABC):

    def __init__(self, product_id, **kwargs):
        super().__init__(product_id, kwargs['name'])

