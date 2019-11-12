import random
import time
import requests
from bs4 import BeautifulSoup
import os


# 请求头
HEADERS = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
    'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0',
    'Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
    )


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
    global HEADERS
    if headers is None:
        headers = random.choice(HEADERS)
    try:
        r = requests.get(url, headers={'User-Agent': headers}, cookies=cookie)
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print(e)
        return None


def get_img_content(img_url):
    """
    函数功能：向服务器请求图片数据
    参数：
        img_url:图片的链接地址
    返回：图片的内容，即图片的二进制数据
    """
    header2 = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
    try:
        r = requests.get(img_url, headers={'User-Agent': header2})
        return r.content
    except Exception as e:
        print(e)


def create_folder(folder_path):
    """
    函数功能：创建目录，如果该目录已存在则直接返回
    参数：
        folder_path:需要创建的目录
    返回：无
    """
    if os.path.exist(folder_path):
        print("该文件夹已存在")
        return
    else:
        os.mkdir(folder_path)


def download_img(img_url, file_path=None, file_name=None):
    """
    函数功能：下载图片
    参数：
        img_url：图片的url链接
        file_path：要保存的图片的目录
        file_name：保存的图片的名称
    返回：无
    """
    img_content = get_img_content(img_url)

    if file_path is None:
        if file_name is None:
            file_name = img_url.split('/')[-1]
        file_path = ''
    with open(file_path + file_name, 'wb')as f:
        f.write(img_content)


def main():
    url = 'https://zhuanlan.zhihu.com/p/89702201'
    cookies_path = 'zhihu_cookies.txt'
    # 保存图片的路径，这里使用相对路径
    img_path = './img/'
    # 从文件中读取并构造字典对象的cookies
    cookies = make_cookies(cookies_path)
    # 构造请求头
    headers = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
    # 获取网页的HTML数据
    html = get_html(url, cookies=cookies, headers=headers)
    if html is None:
        return
    # 转换为bs4对象
    try:
        soup = BeautifulSoup(html, 'html.parser')
        print(soup.title)
    except Exception as e:
        print(e)
    # 获取img标签并去重

    imgs = tuple(soup.find_all('img', class_='origin_image zh-lightbox-thumb lazy'))
    # 解析出标签中的图片链接
    imgs = [i['data-actualsrc'] for i in imgs]
    # 创建保存图片的路径
    create_folder(img_path)
    # 遍历图片的url列表，取出每张图片的链接，下载图片
    for img in imgs:
        # 默认不传入名字，使用网站的图片链接的名字保存图片
        download_img(img_url, file_path=img_path, file_name=None)
        time.sleep(random.randint(3, 6))  # 随机让程序休眠3-6分钟，给服务器喘口气
    print('download over.')


if __name__ == '__main__':
    main()

