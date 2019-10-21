import requests
from bs4 import BeautifulSoup


def get_content(url):
    try:
        r = requests.get(url)
        return r
    except Exception as e:
        print(e)
        return None

base_url = 'https://cn.bing.com'

# response  = requests.get(base_url)
response = get_content(base_url)

soup = BeautifulSoup(response.text, 'html.parser')



#提取源代码中 data-ultra-definition-src 的属性值，然后拼贴到一起

pic_path = soup.find('div', attrs={'id': 'bgImgProgLoad'})['data-ultra-definition-src']

pic_url = base_url + pic_path



# urlretrieve(url=pic_url, filename=r'/Users/linxiaoyue/Desktop/today_wallpaper.jpg')
file_path = "D:\\project\\vs_code_project\\small_spider\\img\\"
img_content = get_content(pic_url).content
with open(file_path + 'test.png', 'wb') as f:
    f.write(img_content)

print('end')
