class GoodsPrice(object):
    id = None
    goods_id = None
    current_price = None
    price = None
    create_time = None

    def __init__(self, goods_id, current_price, price, create_time):
        self.goods_id = goods_id
        self.current_price = current_price
        self.price = price
        self.create_time = create_time
