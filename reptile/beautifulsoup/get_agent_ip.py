import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  #不写这两句会报异常
from bs4 import BeautifulSoup

'''
熊猫人网址：http://www.bbsnet.com/xiongmaoren-18.htm

text 返回的是unicode 型的数据,content返回的是bytes，二级制型的数据
'''

def open_url(url,f12_headers):
    # 返回一个response对象，这个对象里面存的是服务器返回的所有信息，包括响应头，响应状态码等
    response = requests.get(url, headers = f12_headers, verify=False)
    html= response.text
    bs = BeautifulSoup(html, "html.parser")
    # print(bs)
    get_ip(bs)
    # return bs

def get_ip(bs):
    ip_list = bs.find_all("tr")   #bs4的用法
    # print(ip_list)
    for i in  ip_list:
        # print(i.get_text())     #bs4的用法
        f = open('agent_ip.txt','a+',encoding='utf-8')
        f.write(i.get_text())
    print("已保存txt")




if __name__=='__main__':
    # 用F12拿到的请求头，主要是为了伪装成浏览器绕过反爬措施
    f12_headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}
    url ="https://www.kuaidaili.com/free/"

    open_url(url,f12_headers)


