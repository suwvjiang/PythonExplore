#!/usr/bin/env python
# -*- coding: utf-8 -*-

'zcool spider'

__author__="jiangchufei"

import codecs
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://www.zcool.com.cn/'

#打开链接
def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
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
def parse_contain(html):


def main():
    url = DOWNLOAD_URL+'u/333405'
    while url:
        html = download_page(url)
        subpages, url = parse_html(html)
    
    print 'download success'

if __name__ == '__main__':
    main()