#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################
# File Name: TCP编程_server.py
# Created on : 2020-04-14 18:36:11
# Author: cogito0823
# Last Modified: 2020-04-14 18:36:11
# Description:
#########################################################################

import socket
import time
import threading

def tcplink(sock, addr):
    print('Accept new connection from {}:{}...'.format(*addr))
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        else:
            sock.send((f'Hello, {data.decode("utf-8")}!'.encode('utf-8')))
    sock.close()
    print('Connection from {}:{} closed.'.format(*addr))

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print('Waiting for connection...')
    while True:
        sock, addr = s.accept()
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()
