from ProductFactory import ProductFactory
from SantasWorkshop import SantasWorkshop
from Reindeer import Reindeer
from CandyCanes import CandyCanes


class ChristmasProductFactory(ProductFactory):

    def create_toy(self, order):
        product_id = order.details.get('productID')

        product_id = order.product_id
        # collects details of orders
        keys = ['has_batteries', 'min_age', 'name', 'desc', 'dimensions']
        properties = {key: value for key, value in order.details.items() if key in keys}

        order.details['error'] = self.toy_exception(properties)
        if order.details['error'] != "false":
            order.details['corrupted'] = True

        return SantasWorkshop(product_id, properties=properties)

    def create_stuffed_animal(self, order):

        product_id = order.product_id
        product_id = order.details.get('productID')

        # collects details of orders
        keys = ['stuffing', 'size', 'fabric', 'name', 'desc', 'has_glow']
        properties = {key: value for key, value in order.details.items() if key in keys}

        order.details['error'] = self.stuffed_animal_exception(properties)
        if order.details['error'] != "false":
            order.details['corrupted'] = True

        return Reindeer(product_id, properties=properties)

    def create_candy(self, order):
        product_id = order.product_id
        product_id = order.details.get('productID')

        # collects details of orders
        keys = ['has_nuts', 'has_lactose', 'has_lactose', 'desc', 'colour', 'name']
        properties = {key: value for key, value in order.details.items() if key in keys}

        order.details['error'] = self.candy_exception(properties)
        if order.details['error'] != "false":
            order.details['corrupted'] = True

        return CandyCanes(product_id, properties=properties)

        # if exception == "false":
        #
        #
        # else:
        #     return exception

    def toy_exception(self, properties):
        if properties['min_age'] < 0:
            return f"Age must be greater than 0"

        dimensions = str(properties["dimensions"]).split(",")

        if int(dimensions[0]) < 0 and int(dimensions[1]) < 0:
            return "dimensions must be positive"

        return "false"

    def stuffed_animal_exception(self, properties):
        if properties['stuffing'] != 'Polyester Fibrefill' and properties['stuffing'] != 'Wool':
            return "Stuffing can only be Polyester Fiberfill or Wool"

        if properties['size'] != 'S' and properties['size'] != 'M' and properties['size'] != 'L':
            return "size must be either S, M, or L"

        if properties['fabric'] != 'Linen' and properties['fabric'] != 'Cotton' and \
                properties['fabric'] != 'Acrylic':
            return "fabric must be Linen, Cotton, or Acrylic"
        return "false"

    def candy_exception(self, properties):
        if properties['colour'] != 'Red' and properties['colour'] != 'Green':
            return "colour must be Red or Green"

        return "false"
