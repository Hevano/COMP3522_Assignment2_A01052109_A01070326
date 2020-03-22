from ProductFactory import ProductFactory


class HalloweenProductFactory(ProductFactory):

    def create_toy(self, order):
        product_id = order.details.get('productID')
        details = order.details
        # collects details of orders
        keys = [details['hasBatteries'], details['age'], details['name'], details['desc'], details['speed'],
                details['jump_height'], details['does_glow'], details['type']]
        properties = {key: value for key, value in order.details.items() if key in keys}

        return RCSpider(product_id, properties)

    def create_stuffed_animal(self, order):
        product_id = order.details.get('productID')
        details = order.details
        # collects details of orders
        keys = [details['stuffing'], details['size'], details['fabric'], details['name'], details['desc'],
                details['does_glow']]
        properties = {key: value for key, value in order.details.items() if key in keys}

        return DancingSkeleton(product_id, properties)

    def create_candy(self, order):
        product_id = order.details.get('productID')
        details = order.details
        # collects details of orders
        keys = [details['nuts'], details['lactose'], details['name'], details['desc'], details['variety']]
        properties = {key: value for key, value in order.details.items() if key in keys}

        return PumpkinCaramelToffee(product_id, properties)
