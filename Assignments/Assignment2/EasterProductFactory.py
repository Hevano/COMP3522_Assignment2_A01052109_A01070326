from ProductFactory import ProductFactory
from EasterBunny import EasterBunny
from CremeEggs import CremeEggs
from RobotBunny import RobotBunny


class EasterProductFactory(ProductFactory):

    def create_toy(self, order):
        product_id = order.product_id
        # collects details of orders
        keys = ['hasBatteries', 'min_age', 'name', 'desc', 'num_sound', 'colour']
        properties = {key: value for key, value in order.details.items() if key in keys}

        order.details['error'] = self.toy_exception(properties)
        if order.details['error'] != "false":
            order.details['corrupted'] = True

        return RobotBunny(product_id, properties=properties)

    def create_stuffed_animal(self, order):
        product_id = order.product_id
        # collects details of orders
        keys = ['stuffing', 'size', 'fabric', 'name', 'desc', 'colour']
        properties = {key: value for key, value in order.details.items() if key in keys}
        exception = self.stuffed_animal_exception(properties)

        order.details['error'] = self.stuffed_animal_exception(properties)
        if order.details['error'] != "false":
            order.details['corrupted'] = True

        return EasterBunny(product_id, properties=properties)

    def create_candy(self, order):
        product_id = order.product_id
        # collects details of orders
        keys = ['nuts', 'has_lactose', 'name', 'desc', 'pack_size']
        properties = {key: value for key, value in order.details.items() if key in keys}

        order.details['error'] = self.candy_exception(properties)
        if order.details['error'] != "false":
            order.details['corrupted'] = True

        return CremeEggs(product_id, properties=properties)

    def toy_exception(self, properties):
        if properties['min_age'] < 0:
            return "Age must be greater than 0"

        if properties['colour'] != 'Orange' and properties['colour'] \
                != 'Blue' and properties['colour'] != 'Pink':
            return "Colour must be Orange Blue and Pink"

        return "false"

    def stuffed_animal_exception(self, properties):

        if properties['stuffing'] != 'Polyester Fibrefill' and properties['stuffing'] != 'Wool':
            return "Stuffing can only be Polyester Fiberfill or Wool"

        if properties['size'] != 'S' and properties['size'] != 'M' and properties['size'] != 'L':
            return "size must be either S, M, or L"

        if properties['fabric'] != 'Linen' and properties['fabric'] != 'Cotton' and \
                properties['fabric'] != 'Acrylic':
            return "fabric must be Linen, Cotton, or Acrylic"

        if properties['colour'] != 'White' and properties['colour'] != 'Grey' and properties['colour'] \
                != 'Pink' and properties['colour'] != 'Blue':
            return "Colour must be White, Grey, Pink, or blue"

        return "false"

    def candy_exception(self, properties):
        return "false"
