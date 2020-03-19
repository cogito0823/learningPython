#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import request,parse
# 将Form Data信息写入字典
form_data = {
        'i': '肥宅',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '1535101853889',
        'sign': '91ad6b1cd33adeecf92fbd3cc28f0749',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
        }
# 解析form_data字典，得到标准形式
data = parse.urlencode(form_data).encode('utf-8')
url = 'http://fanyi.youdao.com/translate'
req = request.Request(url, data) # 用Request对象传递参数
responce = request.urlopen(req)
html = responce.read().decode()
print(html)
