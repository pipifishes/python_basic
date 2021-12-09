# -*- coding: UTF-8 -*-
from urllib import request
import chardet

url = 'http://www.baidu.com'
response = request.urlopen(url)
html = response.read()

#导入chardet模块，获取编码方式
charset = chardet.detect(html)
print(charset)

# decode()解码
html = html.decode("utf-8")
print(html)