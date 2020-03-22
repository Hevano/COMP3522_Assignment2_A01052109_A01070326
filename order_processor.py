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
        '''
        with(open(path, "r", encoding='utf-8')) as file:
            self.dataFrame = pandas.read_excel(file, index_col=0);
        '''
        self.dataFrame = pandas.read_excel(path, index_col=0);

    def next_order(self):
        for o in self.dataFrame.itertuples():
            factory = OrderProcessor.FACTORIES[o.holiday]
            item = OrderProcessor.ITEMS[o.item]
            ordNo = o.Index
            qty = o.quantity
            name = o.name
            remove = ["Index", "holiday", "item", "quantity", "name"]
            details = {key: value for key, value in o._asdict().items() if key not in remove}
            yield Order(factory, ordNo, item, name, qty, details)


o = OrderProcessor("orders.xlsx")
for order in o.next_order():
    print(order)


