import requests
import random
import warnings



class SpiderDownloader(object):
    # 请求头
    HEADERS = (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36',
        'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0',
        'Mozilla/5.0 (MSIE 10.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
        )

    def html_content(self, url, file_type='html'):
        """
        url: 需要请求的url路径
        file_type: 返回的数据类型，为html格式的字符串
        """
        # 如果传入的url的类型错误，则抛出类型异常
        if url is None:
            raise TypeError("The url type error, url must be string type, not None type.")
        elif type(url) != type('string'):
            raise TypeError("The url type error, url must be string type.")
        else:
            # 如果file_type不为‘html’， 则抛出警告
            if file_type != 'html':
                warnings.warn("The 'file_type' must be html.")
                file_type = 'html'  # 将file_type赋值为'html'
                # raise ValueError("The 'file_type' must be html.")
            # 定制随机请求头，获取response
            response = requests.get(url=url, headers={'User-Agent': random.choice(self.HEADERS)})
            response.encoding = response.apparent_encoding
            # 返回html的字符串格式数据
            return response.text
        return None

    def get_content(self, url):
        """
        url: 需要请求的url路径
        """
        # 如果传入的url的类型错误，则抛出类型异常
        if url is None:
            raise TypeError("The url type error, url must be string type, not None type.")
        elif type(url) != type('string'):
            raise TypeError("The url type error, url must be string type.")
        else:
            # 定制随机请求头，获取response
            response = requests.get(url=url, headers={'User-Agent': random.choice(self.HEADERS)})
            response.encoding = response.apparent_encoding
            # 返回html的字符串格式数据
            return response.content
        return None

    def img_content(self, img_url, file_type='jpg'):
        if img_url is None:
            raise TypeError("The url type error, url must be string type, not None type.")
        elif type(img_url) != type('string'):
            raise TypeError("The url type error, url must be string type.")
        else:
            img_types = ('jpg', 'png', 'jpeg')
            if file_type not in img_types:
                warnings.warn("The 'file_type' must be 'jpg','png', or other image file types.")
                img_type = img_url.split('.')[-1]
                if img_type not in img_types:
                    file_type = 'jpg'
                else:
                    file_type = img_type

            response = requests.get(url=img_url, headers={'User-Agent': random.choice(self.HEADERS)})
            # print(response.status_code)
            # 返回二进制数据
            return response.content
        return None

    def img_downloader(self, img_url, file_type='jpg', file_name=None):
        if img_url is None:
            raise TypeError("The url type error, url must be string type, not None type.")
        elif type(img_url) != type('string'):
            raise TypeError("The url type error, url must be string type.")
        else:
            img_types = ('jpg', 'png', 'jpeg')
            if file_type not in img_types:
                warnings.warn("The 'file_type' must be 'jpg','png', or other image file types.")
                img_type = img_url.split('.')[-1]
                if img_type not in img_types:
                    file_type = 'jpg'
                    img_type = file_type
                else:
                    file_type = img_type

            file_name = img_url.split('/')[-1]

            response = requests.get(url=img_url, headers={'User-Agent': random.choice(self.HEADERS)})

            # print(response.status_code)
            # save the image file and return sucessful code
            with open(file_name, 'wb') as f:
                f.write(response.content)
            return 200
        return None



if __name__ == "__main__":
    pass

