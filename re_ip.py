#!/usr/bin/python3.8.0
# -*- coding-utf-8 -*-
# 由祝荣华编写
import re

str1 = 'Port-channel1.189   192.168.189.254 YES     CONFIG  up'
result1 = re.search('(\w+\-\w+\.\d+)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+\s+(\w+)', str1).groups()
print('-'*80)
print(f'{"接口":<8}:', result1[0])
print(f'{"IP地址":<8}:', result1[1])
print(f'{"状态":<8}:', result1[2])
