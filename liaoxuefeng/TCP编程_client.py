#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################
# File Name: TCP编程_client.py
# Created on : 2020-04-14 18:50:20
# Author: cogito0823
# Last Modified: 2020-04-14 18:50:20
# Description:
#########################################################################

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
while True:
    data = input('Please enter a message: ')
    if not data or data == 'exit':
        s.send(b'exit')
        break
    s.send(data.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))
s.close()
    
