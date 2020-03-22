from StuffedAnimal import StuffedAnimal


class Reindeer(StuffedAnimal):

    def __init__(self, product_id, **kwargs):
        self._details = kwargs
        super().__init__(product_id)

