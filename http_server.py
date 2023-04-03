#!/usr/bin/python3.8.0
# -*- coding-utf-8 -*-
# 由祝荣华编写

from http.server import HTTPServer, CGIHTTPRequestHandler
port = 80
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('Starting simple httpd on port:' + str(httpd.server_port))
httpd.serve_forever()

