#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request,parse
from http import cookiejar

url = 'https://www.zhihu.com/'

headers = {
    'Content-Encoding': 'gzip',
    'cookie': '_xsrf=n2Rk4PrKbcZAJ0NDuvXHfDr4yomAhGsV; z_c0="2|1:0|10:1562506805|4:z_c0|92:Mi4xaHRkakF3QUFBQUFBQU85LW9SR3ZEeVlBQUFCZ0FsVk5OVVFQWGdETEYySTY2MWxzbVo0WHF5SUpmWW1zRy1zQTln|0b04d39c27d10b6a25b549ca252afa0a228cc9adeccc3211c8eb5b81bebb643a"',
    'Sec-Fetch-Mode': 'cors',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
}

req = request.Request(url,headers = headers)

cookie = cookiejar.CookieJar()

handler = request.HTTPCookieProcessor(cookie)

opener = request.build_opener(handler)

responce = opener.open(req)

html = responce.read().decode()

print(html)
