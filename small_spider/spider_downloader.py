import requests
import random


HEADERS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0',
    'Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
    ]


def html_content(url, file_type='html'):
    if url is None:
        raise TypeError("The url type error, url must be string type, not None type.")
    elif type(url) != type('string'):
        raise TypeError("The url type error, url must be string type.")
    else:
        if file_type != 'html':
            raise ValueError("The 'file_type' must be html.")
        response = requests.get(url=url, headers={'User-Agent': random.choice(HEADERS)})
        response.encoding = response.apparent_encoding
        return response.text
    return None




if __name__ == "__main__":
    # test code
    from bs4 import BeautifulSoup
    html = html_content(url='http://www.baidu.com')
    if html is None:
        print("Can't get the html text.")
    else:
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.title.string)

