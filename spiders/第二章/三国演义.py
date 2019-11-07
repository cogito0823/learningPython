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
import string

#小说的保存文件夹
novel_save_dir = os.path.join(os.getcwd(),'novel_cache/')
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

    for href in hrefs[12:]:
        chapter_url_list.append(urllib.parse.urljoin(novel_base_url,href))
    print(chapter_url_list)

def parsing_chapter(url):
    req = urllib.request.Request(url=url,headers=headers)
    html = lxml.html.parse(urllib.request.urlopen(req))
    title = html.xpath('//h1/text()')[0]
    contents = html.xpath('//*[@id="content"]/text()')
    content = ''
    for i in contents[:-2]:
        if '&amp;' in i:
            set1 = i.find('&amp;')
            i = i[:set1] + '\n\n'
        content += i.strip()
    content = content.replace('&1t;/p>','\n\n')
    save_novel(title,content)

def save_novel(name,content):
    try:
        with open(novel_save_dir + name + '.txt',"w+") as f:
            f.write(content.strip())
    except (error.HTTPError,OSError) as reason:
        print(str(reason))
    else:
        print('下载完成：' + name)

if __name__ == '__main__':
    if not os.path.exists(novel_save_dir):
        os.mkdir(novel_save_dir)
    fetch_chapter_urls()
    for chapter in chapter_url_list:
        time.sleep(1)
        parsing_chapter(chapter)
