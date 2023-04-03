#!/usr/bin/python3.8.0
# -*- coding-utf-8 -*-
# 由祝荣华编写

# import os
# import re
# import time
#
# netstat = os.popen('netstat -tulnp').read()
# monitor_port_80 = re.findall('tcp\s+\d+\s+\d+\s+\d+\.\d+\.\d+\.\d+:80\s+', netstat)
# while True:
#     if not monitor_port_80:
#         print('等待一秒重新开始监控!')
#         netstat = os.popen('netstat -tulnp').read()
#         monitor_port_80 = re.findall('tcp\s+\d+\s+\d+\s+\d+\.\d+\.\d+\.\d+:80\s+', netstat)
#         time.sleep(1)
#     else:
#         print('HTTP(TCP/80)服务器已被打开')
#         break

# # 方案一
# list1 = ['aaa', 111, (4, 5), 2.01]
# list2 = ['bbb', 333, 111, 3.14, (4, 5)]
# for x in list1:
#     if x in list2:
#         print(x, ' in List1 and List2')
#     else:
#         print(x, ' only in List1')
#
# # 方案二
# def find(l1, l2):
#     for x in l1:
#         if x in l2:
#             print(x, ' in List1 and List2')
#         else:
#             print(x, ' only in List1')
# find(['aaa', 111, (4, 5), 2.01], ['bbb', 333, 111, 3.14, (4, 5)])

import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *

def qytang_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    if ping_result:
        return True
    else:
        return False

if __name__ == '__main__':
    ip_addr = '192.168.31.1'
    if qytang_ping(ip_addr):
        print(ip_addr, '通！')
    else:
        print(ip_addr, '不通！')
