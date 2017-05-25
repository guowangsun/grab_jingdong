# coding=utf-8


class Config(object):
    host = None
    user = None
    password = None
    db = None

    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db

    def __str__(self):
        return '[host=%s, user=%s, password=%s, db=%s]' % (self.host, self.user, self.password, self.db)
