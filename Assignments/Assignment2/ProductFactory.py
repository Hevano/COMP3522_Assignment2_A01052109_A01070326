import abc
from Toy import Toy
from Candy import Candy
from StuffedAnimal import StuffedAnimal


class ProductFactory(abc.ABC):

    def create(self, order):
        item = None
        if order.item is Toy:
            item = self.create_toy(order)
        elif order.item is StuffedAnimal:
            item = self.create_stuffed_animal(order)
        else:
            item = self.create_candy(order)
        return item

    @abc.abstractmethod
    def create_toy(self, order):
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self, order):
        pass

    @abc.abstractmethod
    def create_candy(self, order):
        pass
