from Candy import Candy


class CandyCanes(Candy):

    def __init__(self, product_id, **kwargs):
        self._details = kwargs
        super().__init__(product_id)

