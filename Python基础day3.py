#!/usr/bin/python3.8.0
# -*- coding-utf-8 -*-
# 由祝荣华编写

import re
str1 = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'
result1 = re.search('(\d+)\s+(\w+\.\w+\.\w+)\s+(\w+)\s+(\w+/\d+/\d+)', str1).groups()
print(f'{"VLAN ID":<11}:', result1[0])
print(f'{"MAC":<11}:', result1[1])
print(f'{"Type":<11}:', result1[2])
print(f'{"Interface":<11}:', result1[3])


# import re
# str1 = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
# result1 = re.search('(\w+)\s+(\w+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)\s+(\w+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+),\s+(\w+)\s+(\d+):(\d+):(\d+),\s+(\w+)\s+(\d+),\s+(\w+)\s+(\w+)', str1).groups()
# print(f'{"protocol":<20}:', result1[0])
# print(f'{result1[1]:<20}:', result1[2])
# print(f'{result1[3]:<20}:', result1[4])
# print(f'{result1[5]:<20}:', f'{result1[6]:<2}小时', f'{result1[7]:<2}分钟', f'{result1[8]:<2}秒')
# print(f'{result1[9]:<20}:', result1[10])
# print(f'{result1[11]:<20}:', result1[12])
