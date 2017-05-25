# coding=utf-8
class ScanConfig(object):
    #
    id = None
    # 京东商品ID
    j_id = None
    # 定时任务表达式
    crontab = None
    # 创建时间
    create_time = None

    def __init__(self, id, j_id, crontab, create_time):
        self.id = id
        self.j_id = j_id
        self.crontab = crontab
        self.create_time = create_time

    def __str__(self):
        return '[id=%s, j_id=%s, crontab=%s, create_time=%s]' % (self.id, self.j_id, self.crontab, self.create_time)

    __repr__ = __str__
