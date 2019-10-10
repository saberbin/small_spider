import requests
from bs4 import BeautifulSoup
from spider_downloader_copy import SpiderDownloader
import os
import re


def create_floder(path):
    pass


def main():
    # url = r'https://www.eb523.com/meinv/list-%E6%8E%A8%E5%A5%B3%E9%83%8E.html'
    url = r'https://www.eb352.com/meinv/list-%E6%8E%A8%E5%A5%B3%E9%83%8E.html'
    spider = SpiderDownloader()
    tuigirl_html = spider.html_content(url)
    # with open('tuigirl.html', 'w', encoding='utf-8') as f:
    #     f.write(tuigirl_html)
    # soup = BeautifulSoup(tuigirl_html, 'html.parser')
    # a_lable = soup.find_all('a')
    # print(a_lable)
    # --------------------------------------------------------------------------------
    r_urls = re.findall(r'/meinv/(\d+).html', tuigirl_html)
    print(r_urls)
    first_url = r_urls[0]
    img_set_url = 'https://www.eb523.com/meinv/{}.html'.format(first_url)
    first_html = spider.html_content(img_set_url)
    # img_soup = BeautifulSoup(first_html, 'html.parser')
    # print(img_soup.title.string)
    # img_urls = img_soup.find_all('img')
    r_img_urls = re.findall(r'https://mmslt1.com/tp/girl/TuiGirl/A-066/(\d+).jpg', first_html)
    print(r_img_urls)
    # img_url = 'https://mmslt1.com/tp/girl/TuiGirl/B-008/02.jpg'
    # spider.img_downloader(img_url)
    

if __name__ == "__main__":
    main()
    

