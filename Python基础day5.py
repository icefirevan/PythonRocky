#!/usr/bin/python3.8.0
# -*- coding-utf-8 -*-
# 由祝荣华编写

# import os
# import re
# route_n_result = os.popen('route -n').read()
# gateway = re.search('[\s\S]*Iface\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+UG[\s\S]*', route_n_result).groups()[0]
# print('网关为:' + gateway)

l1 = [4, 5, 7, 1, 3, 9, 0]
l2 = l1.copy()
l2.sort()
for i in range(len(l1)):
    print(l1[i], l2[i])
