from ProductFactory import ProductFactory


class EasterProductFactory(ProductFactory):

    def create_toy(self, order):
        product_id = order.details.get('productID')
        details = order.details
        # collects details of orders
        keys = [details['hasBatteries'], details['age'], details['name'], details['desc'], details['num_sound'],
                details['colour']]
        properties = {key: value for key, value in order.details.items() if key in keys}

        return RobotBunny(product_id, properties)

    def create_stuffed_animal(self, order):
        product_id = order.details.get('productID')
        details = order.details
        # collects details of orders
        keys = [details['stuffing'], details['size'], details['fabric'], details['name'], details['desc'],
                details['colour']]
        properties = {key: value for key, value in order.details.items() if key in keys}

        return EasterBunny(product_id, properties)

    def create_candy(self, order):
        product_id = order.details.get('productID')
        details = order.details
        # collects details of orders
        keys = [details['nuts'], details['lactose'], details['name'], details['desc'], details['pack_size']]
        properties = {key: value for key, value in order.details.items() if key in keys}

        return CremeEggs(product_id, properties)
