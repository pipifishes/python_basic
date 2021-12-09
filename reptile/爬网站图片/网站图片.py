from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt
import os

print("请把此程序放置在想要保存图片的目录！")
p = str(input("请输入文件夹名称："))
qwer = os.getcwd()

findImgSrc = re.compile(r'<a class="(.*?)" href="//(.*?).jpg"')
xiayiye = re.compile(r'''<a href=".*?">
.* </a>''')

t1 = [0]  # 计数网址
t2 = [0]  # 计数网址
t3 = [0]  # 计数网页爬取图片
t4 = [0]  # 计数文件传入图片


def main():
    try:
        os.mkdir(qwer + "\\" + p)
    except FileExistsError:
        print("文件已存在！")
        os._exit(0)  # 文件关闭
    # 风景
    # urls = "http://jandan.net/ooxx/MjAyMTAxMjUtMg==#comments"
    urls = "http://jandan.net/girl"
    while True:
        url = getData1(urls)
        datalist = getData(url)
        saveData(datalist)
        urls = url


def getData1(url):
    a = 1
    b = t1[0] + a
    t1[0] = b
    # print(url)
    html = askURL(url)
    # print(html)
    print("正在爬取第%d个网址地址" % t1[0])
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all("div", class_="cp-pagenavi"):
        item = str(item)
        # print("正在打印item",item)
        links = re.findall(xiayiye, item)
        # print("正在打印links",links)
        # print("这是下一页的网址links[1]",links[1])
        a = links[1]
        (q, w, e) = a.split('"')
        w = "http:" + w
    return w


def getData(url):
    a = 1
    b = t2[0] + a
    t2[0] = b
    # 获取页面全部信息
    datalist = []
    html = askURL(url)
    # print(html)
    print("正在爬取第%d个网址内容" % t2[0])
    # 逐一解析数据
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all("ol", class_="commentlist"):
        data = []
        item = str(item)
        links = re.findall(findImgSrc, item)
        for link in links:
            a1 = 1
            b1 = t3[0] + a1
            t3[0] = b1
            if link[1] in datalist:
                datalist.remove(link[1])
            datalist.append(link[1])
            print("正在爬取第%d个网址,第%d个图片" % (t2[0], t3[0]))
            # print(link[1])
    return datalist


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    return html


def saveData(datalist):
    a = 1
    b = t4[0] + a
    t4[0] = b
    # print(datalist)
    print("正在传入文件夹....")
    for i in datalist:
        a = 1
        b = t4[0] + a
        t4[0] = b
        print("正在传入第%d张" % t4[0])
        # print(i)
        qwer = os.getcwd()
        qwe = (qwer + "\\" + p + "\\图片%d.jpg" % t4[0])
        i1 = 'http://' + i
        # print(i1)
        img = askURL1(i1)
        with open(qwe, "wb") as f:
            f.write(img)
            print("第%d张已传完！" % t4[0])


def askURL1(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=head)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html


if __name__ == "__main__":
    main()






