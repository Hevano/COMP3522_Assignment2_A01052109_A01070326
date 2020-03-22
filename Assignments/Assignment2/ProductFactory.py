import abc


class ProductFactory(abc.ABC):

    def create(self, order):
        if order.factory is "ChristmasProductFactory":
            self.create_toy(order)
        elif order.factory is "EasterProductFactory":
            self.create_stuffed_animal(order)
        else:
            self.create_candy(order)




    @abc.abstractmethod
    def create_toy(self, order):
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self, order):
        pass

    @abc.abstractmethod
    def create_candy(self, order):
        pass
