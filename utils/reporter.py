#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


class Reporter(object):

    def __init__(self):
        self.sender = 'sender@163.com'
        self.username = 'sender@163.com'
        self.password = 'password'
        self.receiver = ['receiver1@163.com', 'receiver2@163.com', 'receiver3@163.com']
        self.smtp_server = 'smtp.163.com'

    def send_email(self, subject, detail):
        msg = MIMEText(detail, 'plain', 'utf-8')    # 中文需参数‘utf-8’，单字节字符不需要
        msg['From'] = self._format_addr(u'Monitor汇报人 <%s>' % self.sender)
        msg['To'] = self._format_addr(u'开发团队 <%s>' % self.receiver)
        msg['Subject'] = Header(subject, 'utf-8').encode()

        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server)
        # smtp.set_debuglevel(1)    # 打印和SMTP服务器交互的所有信息
        smtp.login(self.username, self.password)
        smtp.sendmail(self.sender, self.receiver.split(','), msg.as_string())
        smtp.quit()

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))


if __name__ == "__main__":
    reporter = Reporter()
    reporter.send_email('python email test', 'hello world')
