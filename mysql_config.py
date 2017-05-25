# coding=utf-8
import os

from connect_error import ConnectError


class Config(object):
    host = None
    user = None
    password = None
    db = None

    def __init__(self):
        self.host = os.environ.get('JING_DONG_MYSQL_HOST')
        self.user = os.environ.get('JING_DONG_MYSQL_USER')
        self.password = os.environ.get('JING_DONG_MYSQL_PASSWORD')
        self.db = os.environ.get('JING_DONG_MYSQL_DB')
        if self.user is None or self.user == '':
            raise ConnectError("用户名为空")
        if self.password is None or self.password == '':
            raise ConnectError("密码为空")
        if self.host is None or self.host == '':
            raise ConnectError("数据库地址为空")
        if self.db is None or self.db == '':
            raise ConnectError("数据库名为空")
