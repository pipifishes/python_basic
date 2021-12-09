from selenium import webdriver
import time
"""
 1. 利用 chromedriver.exe 谷歌浏览器内核
 2. 进入网站
 3. 防止页面加载的太慢，无法找到元素时，
    所设立的等待时间 (3) ———> 每隔0.5秒查找一次元素，共查找6次 即0.5 * 6 = 3 秒
 4. 放入crontab中，每天定时执行
"""
# 模拟浏览器打开网站
driver = webdriver.Chrome("chromedriver.exe")
driver.get(r"https://fishc.com.cn/plugin.php?id=k_misign:sign")
driver.implicitly_wait(3)
# 找到登录窗口，模拟输入用户名密码
driver.find_element_by_css_selector('input[name="username"]').send_keys("pipifish")
driver.find_element_by_css_selector('input[name="password"]').send_keys("GnbajxO4869")
driver.find_element_by_css_selector('button[tabindex="904"]').click()

time.sleep(3)
# 根据路径找到按钮,并模拟进行点击
driver.find_element_by_css_selector('a[id="JD_sign"]').click()
print("签到成功")
# 脚本运行成功,退出浏览器
driver.quit()
