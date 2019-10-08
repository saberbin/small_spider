from bs4 import BeautifulSoup
import requests
from spider_downloader import img_content, html_content


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
    main()