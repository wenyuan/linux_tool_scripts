#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabric.api import *

from utils.reporter import Reporter

# ---------------------参数配置区---------------------
same_password = False    # 登录密码是否相同
if same_password:
    env.user = 'xwy'
    env.hosts = ['192.168.10.1', '192.168.10.2']
    env.password = 'xwy'
else:
    env.hosts = [
        'xwy@192.168.10.1',
        'xwy2@192.168.10.2'
    ]
    env.passwords = {
        'xwy@192.168.10.1:22': 'xwy1',
        'xwy2@192.168.10.2:22': 'xwy2'
    }

disk_check_cmd = 'df -ah'

email_title = u'北京磁盘容量告警'
# ---------------------参数配置区---------------------


@task
def check_disk():
    current_ip = env.host
    result = sudo(disk_check_cmd)
    for line in result.splitlines()[1:]:
        row = line.split()
        fs, total, used, avail, used_percent, mounted_on = row[0], row[1], row[2], row[3], row[4], row[5]
        used_percent = float(used_percent.strip("%")) / 100
        if used_percent > 0.7:
            send_email(current_ip, result)
            break


def send_email(current_ip, result):
    reporter = Reporter()
    email_detail = 'ip: ' + current_ip + '\n\n' + result
    reporter.send_email(email_title, email_detail)
