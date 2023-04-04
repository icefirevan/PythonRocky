#!/usr/bin/python3.9
# -*- coding-utf-8 -*-
# 由祝荣华编写

from Python基础day9 import qytang_ssh
import re
import hashlib
import time

def qytang_get_config(ip='192.168.31.11', username='vincent', password='iCe$135246', port=22, cmd='sh run'):
    try:
        result = qytang_ssh(ip, username, password, port, cmd)
        split_result = re.split(r'\r\nhostname \S+\r\n', result)
        cfg_result = result.replace(split_result[0], '').strip()
        return cfg_result
    except Exception:
        return

def qytang_check_diff(ip):
    before_md5 = ''
    while True:
        cfg_result = qytang_get_config(ip)
        m = hashlib.md5()
        m.update(cfg_result.encode())
        after_md5 = m.hexdigest()
        print(after_md5)
        if not before_md5:
            before_md5 = after_md5
        elif before_md5 != after_md5:
            print('MD5 value changed')
            break
        time.sleep(5)

if __name__ == '__main__':
    # print(qytang_get_config('192.168.31.11'))
    qytang_check_diff('192.168.31.11')