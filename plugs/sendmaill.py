# -*- coding: utf-8 -*-
# @Time    : 2021-04-07 17:21:41
# @Author  : Tibbers
# @File    : Email.py

"""
封装发送邮件的方法

"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class emailmag():
    def emailmags(self):
        my_sender = '360952@163.com'
        my_passwd = ''
        my_user = '@.com.cn'
        my_smtp_host = 'smtp.163.com'  # 163的smtp服务器地址

        msg = MIMEMultipart()
        Subject = '咱家健康测试报告'
        fujian = MIMEText(open('report.html', 'rb').read(), 'html', 'utf-8')
        msg['from'] = my_sender
        msg['to'] = my_user
        msg['subject'] = Subject
        msg.attach(fujian)
        #登陆stmp
        stmp = smtplib.SMTP()
        stmp.connect(my_smtp_host)
        stmp.login(my_sender, my_passwd)
        stmp.sendmail(my_sender, my_user, msg.as_string())
        stmp.quit()


if __name__ == '__main__':
    emailmag().emailmags()
