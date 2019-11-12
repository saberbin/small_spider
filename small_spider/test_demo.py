from bs4 import BeautifulSoup
import requests
from spider_downloader import img_content, html_content, get_content
from fake_useragent import UserAgent
import random


# 请求头
HEADERS = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0',
    'Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
    )

def test_main():
    urls = [
            'http://www.baidu.com',
            'https://w.wallhaven.cc/full/95/wallhaven-95ddex.png'
        ]
    i = 0
    for url in urls:
        content = get_content(url)
        if i == 0:
            with open('a.html', 'wb')as f:
                f.write(content)
        else:
            with open('a.jpg', 'wb') as f:
                f.write(content)
        i = 1

    print('end.')



def small_spider(url, type='html', user_agent=None):
    global HEADERS
    if user_agent is None:
        user_agent = random.choice(HEADERS)
        headers = {'User-Agent':user_agent}
    try:
        r = requests.get(url, headers=headers)
    except Exception as e:
        print(e)
        return
    if type == 'html':
        return r.text
    elif type == 'file':
        return r.content
    else:
        return None




def main():
    url = 'https://sspai.com/'
    html = html_content(url)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.title.string)
    print('-' * 25)
    image_url = 'https://cdn.sspai.com/2019/10/07/9beec9be469d56ef83f03c1f600ce23c.png'
    img_data = img_content(image_url)
    img_type = image_url.split('.')[-1]
    with open('test_demo.{}'.format(img_type), 'wb') as f:
        f.write(img_data)

try:
    response = requests.get('http://www.baidu.com/')
    file_content = response.content
except Exception as e:
    print(e)



if __name__ == "__main__":
    # test_main()
    from random import randint

    x = [randint(0, 100) for i in range(10)]
    y = [randint(0, 100) for i in range(10)]
    print(x)
    print(y)


