import abc
from Item import Item


class Candy(Item, abc.ABC):

    def __init__(self, product_id, **kwargs):
        super().__init__(product_id, kwargs['properties']['name'])
