from ProductFactory import ProductFactory
from EasterBunny import EasterBunny
from RobotBunny import RobotBunny
from CremeEggs import CremeEggs

class EasterProductFactory(ProductFactory):

    def create_toy(self, order):
        product_id = order.product_id
        # collects details of orders
        keys = ['hasBatteries', 'min_age', 'name', 'desc', 'num_sound', 'colour']
        properties = {key: value for key, value in order.details.items() if key in keys}

        return RobotBunny(product_id, properties=properties)

    def create_stuffed_animal(self, order):
        product_id = order.product_id
        # collects details of orders
        keys = ['stuffing', 'size', 'fabric', 'name', 'desc', 'colour']
        properties = {key: value for key, value in order.details.items() if key in keys}

        return EasterBunny(product_id, properties=properties)

    def create_candy(self, order):
        product_id = order.product_id
        # collects details of orders
        keys = ['nuts', 'has_lactose', 'name', 'desc', 'pack_size']
        properties = {key: value for key, value in order.details.items() if key in keys}

        return CremeEggs(product_id, properties=properties)
