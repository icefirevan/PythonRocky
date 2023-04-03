#!/usr/bin/python3.8.0
# -*- coding-utf-8 -*-
# 由祝荣华编写

# import re
#
# asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"
#
# asa_dict = {}
#
# for conn in asa_conn.split('\n'):
#     re_result = re.search('\s*\w+P\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)\s+\w+\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+),\s+\w+\s+\d+:\d+:\d+,\s+\w+\s+(\d+),\s+\w+\s+(\w+)', conn).groups()
#     # print(re_result)
#     asa_dict[(re_result[0], re_result[1], re_result[2], re_result[3])] = (re_result[4], re_result[5])
# print('打印分析后的字典！\n')
# print(asa_dict)
#
# src = 'src'
# src_ip = 'src_ip'
# dst = 'dst'
# dst_ip = 'dst_ip'
# bytes_name = 'bytes'
# flags = 'flags'
# format_str1 = '{:^10}:{:^15}|{:^10}:{:^15}|{:^10}:{:^15}|{:^10}:{:^15}'
# format_str2 = '{:^10}:{:^15}|{:^10}:{:^15}'
#
# print('\n格式化打印输出\n')
#
# for key, value in asa_dict.items():
#     print(format_str1.format(src, key[0], src_ip, key[1], dst, key[2], dst_ip, key[3]))
#     print(format_str2.format(bytes_name, value[0], flags, value[1]))
#     print('=' * 105)

import re

port_list = ['eth 1/101/1/42','eth 1/101/1/26','eth 1/101/1/23','eth 1/101/1/7','eth 1/101/2/46','eth 1/101/1/34','eth 1/101/1/18','eth 1/101/1/13','eth 1/101/1/32','eth 1/101/1/25','eth 1/101/1/45','eth 1/101/2/8']
# print(re.search('eth\s+(\d+)/(\d+)/(\d+)/(\d+)', port_list[0]).groups())
sorted_list = sorted(port_list, key=lambda x:tuple(map(int, re.findall('\d+', x))))
print(sorted_list)

# sorted_list = sorted(port_list, key=lambda x:x)
# print('需要排序的列表:')
# print(port_list)
# print('排序结果:')
# print(sorted_list)



