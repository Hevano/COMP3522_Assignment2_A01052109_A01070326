class Order:

    def __init__(self, factory, orderNo, id, item, name, quantity, details):
        self.factory = factory
        self.orderNo = orderNo
        self.item = item
        self.name = name
        self.quantity = quantity
        self.details = details
        self.product_id = id

