# -*- coding: utf-8 -*-
import datetime
import threading

import MySQLdb
import requests

import send_mail
from goods_message import GoodsMessage
from goods_price import GoodsPrice


def grab_goods(scan_config, db_config):
    thread = threading.Thread(target=grab_goods_and_save(scan_config, db_config))
    thread.start()


def grab_goods_and_save(scan_config, db_config):
    price_json = requests.get("http://p.3.cn/prices/get?skuid=%s" % scan_config.j_id).json()[0]
    print ('j_id %s price_json %s' % (scan_config.j_id, price_json))
    goods_price = GoodsPrice(scan_config.j_id, price_json['op'], price_json['m'], datetime.datetime.utcnow())
    db = MySQLdb.connect(db_config.host, db_config.user, db_config.password, db_config.db)
    cursor = db.cursor()
    insert_sql = 'INSERT INTO goods_price (goods_id, current_price, price, create_time) VALUES (%s, %s, %s, %s)' % (goods_price.goods_id,
                                                                                                                    goods_price.current_price,
                                                                                                                    goods_price.price,
                                                                                                                    goods_price.create_time.strptime(
                                                                                                                        '%Y-%m-%d %H:%M:%S'))
    print ('start insert price %s' % goods_price)
    try:
        cursor.execute(insert_sql)
        db.commit()
        print ('insert success')
    except Exception as e:
        print ('insert error %s' % e)
        db.rollback()
    select_sql = 'SELECT id, j_id, name, url, comment, create_time FROM goods_message WHERE j_id = %s' % scan_config.j_id
    cursor.execute(select_sql)
    result = cursor.fetchall()[0]
    db.close()
    print ('good message %s' % result)
    goods_message = GoodsMessage(result[1], result[2], result[3], result[4], result[5])
    send_mail.send_mail(goods_message, goods_price.current_price)
