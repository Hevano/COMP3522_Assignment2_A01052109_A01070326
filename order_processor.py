import pandas
from order import Order


class OrderProcessor:
    '''
    FACTORIES = {"Christmas": ChristmasProductFactory, "Easter": EasterProductFactory,
                 "Halloween": HalloweenProductFactory}
    ITEMS = {"Toy": Toy, "Candy": Candy,
                 "StuffedAnimal": StuffedAnimal}
    '''

    FACTORIES = {"Christmas": int, "Easter": str,
                 "Halloween": float}
    ITEMS = {"Toy": int, "Candy": str,
             "StuffedAnimal": float}

    def __init__(self, path):
        self.dataFrame = pandas.read_excel(path, index_col=0);

    def next_order(self):
        for o in self.dataFrame.itertuples():
            factory = OrderProcessor.FACTORIES[o.holiday]
            item = OrderProcessor.ITEMS[o.item]
            ordNo = o.Index
            qty = o.quantity
            name = o.name
            id = o.product_id
            remove = ["Index", "holiday", "item", "quantity", "name", "product_id"]
            details = {key: value for key, value in o._asdict().items() if key not in remove}
            yield Order(factory, ordNo, id, item, name, qty, details)



