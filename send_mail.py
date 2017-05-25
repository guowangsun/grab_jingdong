#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText


def send_mail(goods_message, price):
    # 第三方 SMTP 服务
    mail_host = os.environ.get('MAIL_SERVER')  # 设置服务器
    mail_user = os.environ.get('MAIL_USER')  # 用户名
    mail_pass = os.environ.get('MAIL_PASSWORD')  # 口令

    sender = os.environ.get('MAIL_SENDER')
    receivers = [os.environ.get('MAIL_RECEIVE')]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    send_text = goods_message.name + ' ' + price
    message = MIMEText(send_text, 'plain', 'utf-8')
    message['From'] = Header("抓取", 'utf-8')
    message['To'] = Header("孙国旺", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    print ('start send mail')
    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(mail_host, 465)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"
