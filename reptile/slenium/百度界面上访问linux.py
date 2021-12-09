'''
Selenium [səˈliːniəm]
browser: 浏览器
请确保已经正确安装好了 Chrome 浏览器并配置好了 ChromeDriver
用Selenium来驱动浏览器加载网页
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# 声明浏览器对象
browser = webdriver.Chrome()
# 也可以用到其他浏览器，初始化
# browser = webdriver.Firefox()
# browser = webdriver.Edge()
# browser = webdriver.PhantomJS()
# browser = webdriver.Safari()
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('linux')                  # 模拟浏览器中需要输入查询的内容
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)                # 当前的 URL
    # print(browser.get_cookies())            # 当前的 Cookies
    # print(browser.page_source)              # 网页源代码



finally:
    browser.close()
