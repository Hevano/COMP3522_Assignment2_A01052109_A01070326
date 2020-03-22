import abc


class ProductFactory(abc.ABC):

    def create(self, order):
        # code here to choose which factory
        pass
    @abc.abstractmethod
    def create_toy(self, order):
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self, order):
        pass

    @abc.abstractmethod
    def create_candy(self, order):
        pass
