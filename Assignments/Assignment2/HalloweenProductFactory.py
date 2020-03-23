from ProductFactory import ProductFactory
from DancingSkeleton import DancingSkeleton
from RCSpider import RCSpider
from PumpkinCaramelToffee import PumpkinCaramelToffee


class HalloweenProductFactory(ProductFactory):

    def create_toy(self, order):
        product_id = order.product_id
        # collects details of orders
        keys = ['has_batteries', 'min_age', 'name', 'desc', 'speed',
                'jump_height', 'has_glow', 'type', 'spider_type']
        properties = {key: value for key, value in order.details.items() if key in keys}

        order.details['error'] = self.toy_exception(properties)
        if order.details['error'] != "false":
            order.details['corrupted'] = True

        return RCSpider(product_id, properties=properties)

    def create_stuffed_animal(self, order):
        product_id = order.product_id
        # collects details of orders
        keys = ['stuffing', 'size', 'fabric', 'name', 'desc',
                'has_glow', 'jump_height']
        properties = {key: value for key, value in order.details.items() if key in keys}
        exception = self.stuffed_animal_exception(properties)

        order.details['error'] = self.stuffed_animal_exception(properties)
        if order.details['error'] != "false":
            order.details['corrupted'] = True

        return DancingSkeleton(product_id, properties=properties)

    def create_candy(self, order):
        product_id = order.product_id
        # collects details of orders
        keys = ['nuts', 'lactose', 'name', 'desc', 'variety']
        properties = {key: value for key, value in order.details.items() if key in keys}

        order.details['error'] = self.candy_exception(properties)
        if order.details['error'] != "false":
            order.details['corrupted'] = True

        return PumpkinCaramelToffee(product_id, properties=properties)

    def toy_exception(self, properties):
        if properties['min_age'] < 0:
            return "Age must be greater than 0"
        if properties['has_glow'] != 'Y' and properties['has_glow'] != 'N':
            return "has_glow must be Y and N"
        if properties['spider_type'] != 'Tarantula' and properties['spider_type'] != 'Wolf Spider':
            return "Spider type must be Tarantula and Wolf Spider"

        return "false"

    def stuffed_animal_exception(self, properties):
        if properties['stuffing'] != 'Polyester Fibrefill' and properties['stuffing'] != 'Wool':
            return "Stuffing can only by Polyester Fiberfill or Wool"

        if properties['size'] != 'S' and properties['size'] != 'M' and properties['size'] != 'L':
            return "size must be either S, M, or L"

        if properties['fabric'] != 'Linen' and properties['fabric'] != 'Cotton' and \
                properties['fabric'] != 'Acrylic':
            return "size must be either S, M, or L"

        if properties['has_glow'] != 'Y' and properties['has_glow'] != 'N':
            return "has_glow must be Y or N"

        return "false"

    def candy_exception(self, properties):
        if properties['variety'] != 'Sea Salt' and properties['variety'] != 'Regular':
            return "variety Sea Salt or Regular"
