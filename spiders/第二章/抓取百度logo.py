#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

pic_url = 'https://www.baidu.com/img/bd_logo1.png'
pic_resp = urllib.request.urlopen(pic_url)
pic = pic_resp.read()
with open('bd_logo.png','wb') as f:
    f.write(pic)
