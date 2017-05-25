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

    def __str__(self):
        return '[id=%s, goods_id=%s, current_price=%s, price=%s, create_time=%s]' % (self.id, self.goods_id,
                                                                                     self.current_price, self.price, self.create_time)
