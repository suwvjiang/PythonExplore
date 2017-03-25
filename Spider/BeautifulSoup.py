#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Beautiful Soup'

__author__="jiangchufei"

import bs4
import codecs
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://movie.douban.com/top250'#'https://www.chiphell.com/portal.php'

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

def parse_html(html):
    soup = BeautifulSoup(html)
    movie_list_soup = soup.find('ol', attrs={'class':'grid_view'})
    movie_name_list = []
    for li in movie_list_soup.find_all('li'):
        detail = li.find('div', attrs={'class':'hd'})
        movie_name = detail.find('span', attrs={'class':'title'}).string
        movie_name_list.append(movie_name)

    next_page = soup.find('span', attrs={'class':'next'}).find('link')
    if next_page:
        return movie_name_list, DOWNLOAD_URL+next_page['href']
    return movie_name_list, None

def main():
    url = DOWNLOAD_URL
    with codecs.open('movies.txt', 'wb', encoding='utf-8') as fp:
        while url:
            html = download_page(url)
            movies, url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))
            print(u'{movies}\n'.format(movies='\n'.join(movies)))
    print 'download success'

if __name__ == '__main__':
    main()