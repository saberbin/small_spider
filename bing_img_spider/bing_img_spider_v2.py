import requests
from bs4 import BeautifulSoup
import random
import time
import sys


HEADERS = (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0',
        'Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
        )


def get_content(url):
    global HEADERS
    try:
        r = requests.get(url, headers={'User-Agent': random.choice(HEADERS)})
        return r
    except Exception as e:
        print('Got a error:', e)
        return None

def main(file_name):

    base_url = 'https://cn.bing.com'

    # response  = requests.get(base_url)
    response = get_content(base_url)
    if response is None:
        print("The response is None.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    #提取源代码中 data-ultra-definition-src 的属性值，然后拼贴到一起
    pic_path = soup.find('div', attrs={'id': 'bgImgProgLoad'})['data-ultra-definition-src']
    # print(pic_path)
    pic_url = base_url + pic_path

    file_path = '.\\img\\'
    if not file_name:
        file_name = '%6d'%random.randint(10000, 999999)
    img_content = get_content(pic_url).content
    with open(file_path + file_name + '.jpg', 'wb') as f:
        f.write(img_content)


if __name__ == '__main__':
    file_name = sys.argv[1]
    main(file_name)
    print('end')
