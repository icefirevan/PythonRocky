#!/usr/bin/python3.8.0
# -*- coding-utf-8 -*-
# 由祝荣华编写

import logging
logging.getLogger('kamene.runtime').setLevel(logging.ERROR)
from kamene.all import *
import paramiko
import ipaddress

from Python基础day8 import qytang_ping
from Python基础day9 import qytang_ssh
# ip1 = '192.168.31.11'
# username1 = 'vincent'
# password1 = 'iCe$135246'
def get_int_info(ip, username, password, port=22, cmd='sh ip int b'):
    if qytang_ping(ip):
        int_info = qytang_ssh(ip, username, password, port, cmd)
        return int_info

# x = get_int_info(ip1, username1, password1)
# print(x)

if __name__ == '__main__':
    for ip_addr in ipaddress.IPv4Network('192.168.31.0/24'):
        try:
            ip_addr_str = str(ip_addr)
            if get_int_info(ip_addr_str, 'vincent', 'iCe$135246'):
                print(get_int_info(ip_addr_str, 'vincent', 'iCe$135246'))
        except paramiko.ssh_exception.NoValidConnectionsError:
            print(r"Can't SSH to " + ip_addr_str)
