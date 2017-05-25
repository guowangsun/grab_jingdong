# -*-coding:utf-8 -*-

import datetime
import os
import sched
import threading
import time

import MySQLdb
from crontab import CronTab

import grab
from mysql_config import Config
from scan_config import ScanConfig


class Main(object):
    schedule = sched.scheduler(time.time, time.sleep)
    scanConfigs = []
    start_flag = False
    dbConfig = None

    def __init__(self, inc):
        self.dbConfig = Config(os.environ.get('JING_DONG_MYSQL_HOST'), os.environ.get('JING_DONG_MYSQL_USER'),
                               os.environ.get('JING_DONG_MYSQL_PASSWORD'), os.environ.get('JING_DONG_MYSQL_DB'))
        self.schedule.enter(0, 0, self.start, (inc,))
        self.schedule.run()

    def start(self, inc):
        db = MySQLdb.connect(self.dbConfig.host, self.dbConfig.user, self.dbConfig.password, self.dbConfig.db, charset='utf8')
        cursor = db.cursor()
        sql = 'SELECT id, j_id, crontab, create_time FROM scan_config'
        print ('reload scan_config start')
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            temp_scan_conifgs = []
            for row in result:
                temp_scan_conifgs.append(ScanConfig(row[0], row[1], row[2], row[3]))
            self.scanConfigs = temp_scan_conifgs
        except Exception as e:
            print ('Error : read mysql error', e)
        db.close()
        print ('reload scan_config end, scan config : %s' % self.scanConfigs)
        if self.start_flag is False:
            self.start_flag = True
            print ('start scan config')
            thread = threading.Thread(target=self.scan_crontab, name='scan_crontab_thread')
            thread.setDaemon(True)
            thread.start()

        self.schedule.enter(inc, 0, self.start, (inc,))

    def scan_crontab(self):
        while True:
            now = datetime.datetime.utcnow()
            for scanConfig in self.scanConfigs:
                ct = CronTab(scanConfig.crontab)
                delay = ct.next(now, default_utc=True)
                print ('now %s, scan_config %s, delay %s' % (now, scanConfig, delay))
                if delay < 1:
                    grab.grab_goods(scanConfig, self.dbConfig)
            time.sleep(1)


if __name__ == '__main__':
    main = Main(60)
