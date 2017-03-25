#!/usr/bin/env python
# -*- coding: utf-8 -*-

'zcool spider'

__author__="jiangchufei"

import os
import codecs
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://www.zcool.com.cn/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
}

imgPath = os.path.join('.', 'image')

#打开链接
def download_page(url):
    data = requests.get(url, headers=headers).content
    return data

#解析母页
def parse_html(html):
    soup = BeautifulSoup(html)
    con = soup.find('div', attrs={'class':'camWholeBox borderTop'})
    arts_list_soup = con.find('ul', attrs={'class':'layout camWholeBoxUl'})
    arts_url_list = []
    for li in arts_list_soup.find_all('li'):
        detail = li.find('div', attrs={'class':'camLiTitleC hot'})
        arts_url = detail.a['href']
        print arts_url
        arts_url_list.append(arts_url)

    next_page = soup.find('div', attrs={'class':'borderTop'}).find('a', attrs={'class':'pageNext'})
    if next_page and next_page.has_attr('href'):
        return arts_url_list, DOWNLOAD_URL+next_page['href']
    return arts_url_list, None

#解析子页并保存图片
def parse_subpage(html):
    soup = BeautifulSoup(html)
    total = soup.find('div', attrs={'class':'workContentWrapper borderTop'})
    if total:
        content = total.find('div', attrs={'class':'workContent layout f16 c666'})
        if content:
            for url in content.find_all('img'):
                name = os.path.split(url['src'])[1]
                img = requests.get(url['src'], headers=headers)
                #写入多媒体文件必须要 b 这个参数！！
                f = open(name, 'ab')
                #多媒体文件要是用conctent
                f.write(img.content)
                f.close()
                print 'success save%s'%name

def main():
    url = DOWNLOAD_URL+'u/333405'
    #创建目录
    if not os.path.exists(imgPath):
        os.mkdir(imgPath)
    #切换目录
    os.chdir(imgPath)

    subpages = []
    while url:
        html = download_page(url)
        result = parse_html(html)
        subpages.extend(result[0])
        url = result[1]

    for page in subpages:
        html = download_page(page)
        parse_subpage(html)

    print 'download success'

if __name__ == '__main__':
    main()