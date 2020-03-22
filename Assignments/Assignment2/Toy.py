import abc


class Toy(abc.ABC):

    def __init__(self, product_id, **kwargs):
        self._product_id = product_id
