from bs4 import BeautifulSoup
import requests
from spider_downloader import img_content, html_content, get_content


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



if __name__ == "__main__":
    # test_main()
    from random import randint

    x = [randint(0, 100) for i in range(10)]
    y = [randint(0, 100) for i in range(10)]
    print(x)
    print(y)
