class GoodsPrice(object):
    id = None
    j_id = None
    current_price = None
    price = None
    create_time = None

    def __init__(self, j_id, current_price, price, create_time):
        self.j_id = j_id
        self.current_price = current_price
        self.price = price
        self.create_time = create_time

    def __str__(self):
        return '[id=%s, goods_id=%s, current_price=%s, price=%s, create_time=%s]' % (self.id, self.j_id,
                                                                                     self.current_price, self.price, self.create_time)

    __repr__ = __str__
