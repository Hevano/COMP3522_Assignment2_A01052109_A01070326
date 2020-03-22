from ProductFactory import ProductFactory


class ChristmasProductFactory(ProductFactory):

    def create_toy(self, order):
        has_batteries = order.dict.get('hasBatteries')
        age = order.dict.get('age')
        name = order.dict.get('name')
        desc = order.dict.get('desc')
        product_id = order.dict.get('productID')
        dimensions = order.dict.get('dimensions')
        return santas_workshop(has_batteries, age, name, desc, product_id, dimensions)

    def create_stuffed_animal(self, order):
        stuffing = order.dict.get('stuffing')
        size = order.dict.get('size')
        fabric = order.dict.get('fabric')
        name = order.dict.get('name')
        desc = order.dict.get('desc')
        product_id = order.dict.get('productID')



    def create_candy(self, order):








