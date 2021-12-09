#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  #不写这两句会报异常
'''
需要导入lxml模块

神墓小说：http://www.biqukan.com/3_3039/

text 返回的是unicode 型的数据,content返回的是bytes，二级制型的数据

BeautifulSoup.select:标签名不加任何修饰，类名前加点，id名前加 #，在这里我们也可以利用类似的方法来筛选元素，用到的方法是 soup.select()，返回类型是 list
BeautifulSoup.find:为了找到BeautifulSoup对象内任何第一个标签入口，使用find()方法
'''

# 用F12拿到的请求头，主要是为了伪装成浏览器绕过反爬措施
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
# 获取网址的html结构
url = 'https://www.bqktxt.com/3_3039/'
response = requests.get(url=url, headers=headers, verify=False)
response.encoding = "gbk"
html_text = response.text
# print(html_text)

# 获取文章目录的html结构
soup = BeautifulSoup(html_text, 'lxml')  # lxml解析
li_list = soup.select('.listmain > dl > dd')  # 用来获取目录 ,这步是对html_text内容，通过类名+属性查找目录
print(li_list)

# 创建存放将要抓取的文件
if not os.path.exists('./神墓'):
    os.mkdir('./神墓')

for i in li_list:            # 遍历所有的li标签.里面包含有连接和标题
    title = i.a.string       # 获取章节标题
    # print(title)

    # 拼接得到每一章节的url,获取正文的html结构
    info_url = 'https://www.bqktxt.com/'+i.a['href']
    info_response = requests.get(info_url, headers=headers,verify=False)
    info_response.encoding = "gbk"
    info_text = info_response.text
    # print(info_text)

    info_soup = BeautifulSoup(info_text, 'lxml')  # 还是lxml解析
    div_tag = info_soup.find('div', class_='showtxt')  # 定位内容部分标签.
    data_text = div_tag.get_text()  # 获取正文部分
    # print(data_text)

    f = open(f"./神墓/{title}.txt", 'w', encoding='utf-8')  # 创建章节目录，一章就是一个txt
    f.write(f"{title}\n{data_text}\n")  # 写入标题加对应正文.换行符隔开
    print(f"{title}",'爬取写入完成.')
