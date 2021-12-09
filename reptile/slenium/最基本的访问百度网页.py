from selenium import webdriver
'''
请确保已经正确安装好了 Chrome 浏览器并配置好了 ChromeDriver
1. 最基本的网页访问
'''
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
print(browser.page_source)          # 网页源代码
browser.close()
