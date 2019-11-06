#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
from urllib import error
from lxml import etree
import lxml.html
import os
import time

#小说站点的URL
novel_base_url = 'http://www.biqukan.com'

#获取小说的URL
novel_url = urllib.parse.urljoin(novel_base_url,'/50_50096/')

chapter_url_list = []

headers = {
    'Host': 'www.biqukan.com',
    'Referer': 'http://www.biqukan.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; lntel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

def fetch_chapter_urls():
    req = urllib.request.Request(url=novel_url,headers=headers)
    html = lxml.html.parse(urllib.request.urlopen(req))
    hrefs = html.xpath('//dd/a/@href')

    for href in hrefs[16:]:
        chapter_url_list.append(urllib.parse.urljoin(novel_base_url,href))
    print(chapter_url_list)

if __name__ == '__main__':
    fetch_chapter_urls()
