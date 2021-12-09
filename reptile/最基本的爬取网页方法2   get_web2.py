import requests
# 用F12拿到的请求头，主要是为了伪装成浏览器绕过反爬措施
f12_headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
url ="https://blog.csdn.net/baichoufei90/article/details/83594212"
# 返回一个response对象，这个对象里面存的是服务器返回的所有信息，包括响应头，响应状态码等
response = requests.get(url, headers = f12_headers, verify=False)
print(response.text)