#!/usr/bin/python3.8.0
# -*- coding-utf-8 -*-
# 由祝荣华编写

import paramiko

def qytang_ssh(ip, username, password, port=22, cmd='sh ip int b'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    ssh.connect(ip, port, username, password, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

import re

def ssh_get_route(ip, username, password):
    route_n_result = qytang_ssh(ip, username, password, port=22, cmd='route -n')
    gateway = re.search(
        '[\s\S]*Iface\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+UG[\s\S]*',
        route_n_result).groups()[0]
    return gateway

# print(qytang_ssh('192.168.31.11', 'vincent', 'iCe$135246'))

# if __name__ == '__main__':
#     print(qytang_ssh('192.168.31.230', 'root', 'ice831129'))
#     print(qytang_ssh('192.168.31.230', 'root', 'ice831129', cmd='pwd'))
#     print('网关为:')
#     print(ssh_get_route('192.168.31.230', 'root', 'ice831129'))
