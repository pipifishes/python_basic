from selenium import webdriver
import time  # 后续延时加载需要用到
"""
 1. 利用 chromedriver.exe 谷歌浏览器内核
 2. 进入网站
 3. 防止页面加载的太慢，无法找到元素时，
    所设立的等待时间 (3) ———> 每隔0.5秒查找一次元素，共查找6次 即0.5 * 6 = 3 秒
 4. 放入crontab中，每天定时执行
"""

# 模拟浏览器打开网站
browser = webdriver.Chrome()
browser.get('https://fishc.com.cn/plugin.php?id=k_misign:sign')
browser.implicitly_wait(3)

# 输入账号密码 点击登录
browser.find_element_by_xpath('//*[@id="ls_username"]').send_keys('pipifish')
browser.find_element_by_xpath('//*[@id="ls_password"]').send_keys('GnbajxO4869')
browser.find_element_by_xpath('//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button/em').click()
time.sleep(2)

# 根据路径找到按钮,并模拟进行点击
browser.find_element_by_xpath('//*[@id="JD_sign"]').click()
print("签到成功")
browser.quit()

