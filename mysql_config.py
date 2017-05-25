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
