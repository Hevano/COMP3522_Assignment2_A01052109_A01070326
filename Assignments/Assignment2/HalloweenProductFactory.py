from ProductFactory import ProductFactory
from DancingSkeleton import DancingSkeleton
from RCSpider import RCSpider
from PumpkinCaramelToffee import PumpkinCaramelToffee


class HalloweenProductFactory(ProductFactory):

    def create_toy(self, order):
        product_id = order.details.get('productID')
        # collects details of orders
        keys = ['has_batteries', 'min_age', 'name', 'desc', 'speed',
                'jump_height', 'has_glow', 'type', 'spider_type']
        properties = {key: value for key, value in order.details.items() if key in keys}

        return RCSpider(product_id, properties=properties)

    def create_stuffed_animal(self, order):
        product_id = order.details.get('productID')
        # collects details of orders
        keys = ['stuffing', 'size', 'fabric', 'name', 'desc',
                'has_glow', 'jump_height']
        properties = {key: value for key, value in order.details.items() if key in keys}

        return DancingSkeleton(product_id, properties=properties)

    def create_candy(self, order):
        product_id = order.details.get('productID')
        # collects details of orders
        keys = ['nuts', 'lactose', 'name', 'desc', 'variety']
        properties = {key: value for key, value in order.details.items() if key in keys}

        return PumpkinCaramelToffee(product_id, properties=properties)
