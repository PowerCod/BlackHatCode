#! /usr/bin/env python
#coding=utf-8

import socket

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("afaf", (target_host, target_port))

data = client.recvfrom(4096)

print data