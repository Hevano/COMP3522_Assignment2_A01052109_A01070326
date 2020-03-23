import abc
from Toy import Toy
from Candy import Candy
from StuffedAnimal import StuffedAnimal


class ProductFactory(abc.ABC):

    def create(self, order):
        if order.item is Toy:
            self.create_toy(order)
        elif order.item is StuffedAnimal:
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
