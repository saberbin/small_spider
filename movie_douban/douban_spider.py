import requests
from bs4 import BeautifulSoup
import random
import os
import time


HEADERS = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0',
    'Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
    )

# Cookie: bid=knMOJ3Nlpr8; douban-fav-remind=1; ll="118281"; __utma=30149280.143176519.1574575638.1574575638.1574575638.1; __utmb=30149280.0.10.1574575638; __utmc=30149280; __utmz=30149280.1574575638.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.1343588672.1574575638.1574575638.1574575638.1; __utmb=223695111.0.10.1574575638; __utmc=223695111; __utmz=223695111.1574575638.1.1.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; _pk_ses.100001.4cf6=*; __yadk_uid=cdoUVLTYmwcKjAqdJJW4YrTWMiPY9PS5; _vwo_uuid_v2=D1FD78E494E0A5E16D76D27C810167B70|6620d50f1d0f300ff917920e854b769f; dbcl2="170987053:4H84xudGN7Y"; ck=MEng; push_noty_num=0; push_doumail_num=0; _pk_id.100001.4cf6=9356e3931560b08b.1574575652.1.1574575733.1574575652.

def make_cookies(cookies_path):
    """
    函数功能：构造特定用户的cookies
    参数：保存cookies的txt文件目录
    返回：cookies的字典对象
    """
    cookies = dict()
    with open(cookies_path, 'r')as f:
        data = f.read()
    for line in data.split(';'):
        key, value = line.split('=', 1)  # 指定分割次数为1，否则会报错
        cookies[key] = value
    return cookies


def get_html(url, cookies=None, headers=None):
    """
    函数功能：向服务器请求特定url的页面
    参数：
        url：链接地址
        cookies：该网站的用户的cookies
        headers：构造的请求头
    返回：响应的文本内容，即HTML数据
    """
    # user-agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.45 Safari/537.36 Edg/79.0.309.30'
    global HEADERS
    if headers is None:
        # headers = random.choice(HEADERS)
        headers = HEADERS[0]
    try:
        r = requests.get(url, headers={'User-Agent': headers}, cookies=cookies)
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        print(e)
        return None

def parser(soup):
    div_list = soup.find_all('div', _class='hd')
    return div_list


def main():
    url = 'https://movie.douban.com/top250?start={}&filter='
    # url = 'https://movie.douban.com/top250'
    # cookies_path = 'cookies.txt'
    cookies_path = r'D:\\project\\vs_code_project\\small_spider\\movie_douban\\cookies.txt'
    cookies = make_cookies(cookies_path)
    for i in range(10):
        url = url.format(str(i * 25))
        # start = i * 25
        html = get_html(url, cookies=cookies, headers=None)
        try:
            soup = BeautifulSoup(html, 'html.parser')
            print(soup.title.string)
        except Exception as e:
            print(e)
        time.sleep(5)
    # with open('douban.html', 'w', encoding='UTF-8') as f:
    #     f.write(html)
    


if __name__ == "__main__":
    main()
    # files = os.listdir()
    # print(files)  # ['.git', '.gitignore', '.vscode', 'bing_img_spider', 'LICENSE', 'movie_douban', 'README.md', 'small_spider', 'zhihu_img_spaider']
    # pass

