class GoodsMessage(object):
    id = None
    j_id = None
    name = None
    url = None
    comment = None
    create_time = None

    def __init__(self, j_id, name, url, comment, create_time):
        self.j_id = j_id
        self.name = name
        self.url = url
        self.comment = comment
        self.create_time = create_time
