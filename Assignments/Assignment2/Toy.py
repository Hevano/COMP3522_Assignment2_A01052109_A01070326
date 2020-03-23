import abc
from Item import Item


class Toy(abc.ABC, Item):

    def __init__(self, product_id, **kwargs):
        super().__init__(product_id, kwargs['name'])

