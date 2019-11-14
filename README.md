# small_spider
small_spider



## 使用方法

`bing_img_spider_v2.py`为必应背景图片爬虫。

环境：`python3.7 + requests + BeautifulSoup`

执行方法：

在命令行运行：

`python bing_img_spider_v2.py file_name`或者`python3 bing_img_spider_v2.py file_name`

例如：`python bing_img_spider_v2.py aaa `

会在当前脚本的`img`文件夹保存`aaa.jpg`的图片。

> `bing_img_spider_v2.py`在执行的时候需要接收一个参数，作为需要保存的图片文件的名称。
> `bing_img_spider_v2_1.py`为`bing_img_spider_v2.py`的后续版本，这里改进的图片文件的保存的代码，以当前日期随机拼接字母为文件名保存图片文件，如`2019-11-13_q.jpg`