from Toy import Toy


class RCSpider(Toy):

    def __init__(self, product_id, **kwargs):
        self._details = kwargs
        super().__init__(product_id)
