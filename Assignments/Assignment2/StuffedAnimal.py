import abc
from Item import Item


class StuffedAnimal(Item, abc.ABC):

    def __init__(self, product_id, **kwargs):
        super().__init__(product_id, kwargs['properties']['name'])
