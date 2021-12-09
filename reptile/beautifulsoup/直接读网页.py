# -*- coding: UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
# 如果是读一个文件用这种
# file = open('./a.html', 'rb')     # rb：以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头
# html = file.read()

#直接读网页
url = 'http://www.baidu.com'
response = request.urlopen(url)
html = response.read()
bs = BeautifulSoup(html,"html.parser") # 缩进格式
# print(bs.prettify()) # 格式化html结构
print(bs.title) # 获取title标签的内容
print(bs.title.name) # 获取title的name
print(bs.title.string) # 获取head标签的所有内容/获取标签内部的文字
# print(bs.head)
# print(bs.div)  # 获取第一个div标签中的所有内容
# print(bs.div["id"]) # 获取第一个div标签的id的值   bs.div["id"]=bs.div.get('id')
# print(bs.a)
print(bs.find_all("a")) # 获取所有的a标签
# print(type(bs.find_all("a")))   # bs4.element.ResultSet,  这里是字典外套了一个列表
# print(bs.find(id="u1")) # 获取id="u1"
for item in bs.find_all("a"):
    print(item.get("href")) # 获取所有的a标签，并遍历打印a标签中的href的值
for item in bs.find_all("a"):
    print(item.get_text())