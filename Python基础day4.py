#!/usr/bin/python3.8.0
# -*- coding-utf-8 -*-
# 由祝荣华编写

import os
import re

ifconfig_result = os.popen('ifconfig ' + 'enp0s3').read()

# 正则表达式查找IP，掩码，广播和mac地址
ipv4_add = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ifconfig_result)[0]
netmask = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ifconfig_result)[1]
broadcast = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ifconfig_result)[2]
mac_addr = re.findall('\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}', ifconfig_result)[0]

# 格式化字符串
format_string = '{:<10}:{}'

# 打印结果
print(format_string.format('ipv4_add', ipv4_add))
print(format_string.format('netmask', netmask))
print(format_string.format('broadcast', broadcast))
print(format_string.format('mac_addr', mac_addr))

# 产生网关的IP地址
ipv4_element = re.findall('\d{1,3}\.', ipv4_add)
ipv4_gw = ipv4_element[0] + ipv4_element[1] + ipv4_element[2] + '1'

# 打印网关的IP地址
print('\n我们假定网关IP地址为最后一位为1，因此网关IP地址为:' + ipv4_gw + '\n')

# Ping网关
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()

re_ping_result = re.findall('\s+0%\s+packet\s+loss', ping_result)

if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')
