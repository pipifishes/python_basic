import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  #不写这两句会报异常
'''
熊猫人网址：http://www.bbsnet.com/xiongmaoren-18.htm

text 返回的是unicode 型的数据,content返回的是bytes，二级制型的数据
'''
# 用F12拿到的请求头，主要是为了伪装成浏览器绕过反爬措施
f12_headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
url ="http://www.bbsnet.com/richang-3.html"
# 返回一个response对象，这个对象里面存的是服务器返回的所有信息，包括响应头，响应状态码等
response = requests.get(url, headers = f12_headers, verify=False)
# print(response.text)


#需要用正则匹配所有的图片，根据上述可以看到  "http://*********.gif"
src = re.findall(r'http://wx4.sinaimg.cn/.*?gif',response.text)
#print(type(src))
#print(src)

count=0
for i in src:
    # img_file = response.content  #这些下载的图片会打不开
    img_file  = requests.get(i, headers = f12_headers, verify=False).content  #因为是图片格式，bytes    同时需要更换url
    count+=1
    filename=str(count)
    # 以下3中方式都行
    # with open('./%s.png' % filename, 'wb')as f:
    #     f.write(img_file)
    # with open(f'{filename}.jpg','wb')as f:
    #      f.write(img_file)
    file = open(f'./test/{filename}.gif','wb')
    file.write(img_file)
    print(f"第{filename}张已下载")
print("over")