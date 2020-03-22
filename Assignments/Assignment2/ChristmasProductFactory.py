from ProductFactory import ProductFactory
from SantasWorkshop import SantasWorkshop
from Reindeer import Reindeer
from CandyCanes import CandyCanes


class ChristmasProductFactory(ProductFactory):

    def create_toy(self, order):
        # has_batteries = order.details.get('hasBatteries')
        # age = order.details.get('age')
        # name = order.details.get('name')
        # desc = order.details.get('desc')
        # dimensions = order.details.get('dimensions')
        product_id = order.details.get('productID')
        details = order.details

        # collects details of orders
        keys = [details['hasBatteries'], details['age'], details['name'], details['desc'], details['dimensions']]
        properties = {key: value for key, value in order.details.items() if key in keys}

        return SantasWorkshop(product_id, properties)

    def create_stuffed_animal(self, order):

        # stuffing = order.details.get('stuffing')
        # size = order.details.get('size')
        # fabric = order.details.get('fabric')
        # name = order.details.get('name')
        # desc = order.details.get('desc')
        # nose_glow = order.details.get('noseGlow')
        product_id = order.details.get('productID')
        details = order.details

        # collects details of orders
        keys = [details['stuffing'], details['size'], details['fabric'], details['name'], details['desc'], details['noseGlow']]
        properties = {key: value for key, value in order.details.items() if key in keys}

        return Reindeer(product_id, properties)

    def create_candy(self, order):
        product_id = order.details.get('productID')
        details = order.details
        # collects details of orders
        keys = [details['nuts'], details['lactose'], details['name'], details['desc'], details['stripes']]
        properties = {key: value for key, value in order.details.items() if key in keys}

        return CandyCanes(product_id, properties)












