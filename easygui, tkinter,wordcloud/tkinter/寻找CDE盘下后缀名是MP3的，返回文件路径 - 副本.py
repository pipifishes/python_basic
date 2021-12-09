import os
import tkinter as tk
# from pandas import read_excel
import pandas as pd
from random import randint
'''
先查找CDE盘目录下所有mp3文件
保存成文本
调窗口显示mp3文件路径
打包成exe文件
'''
'''
1. os.walk() 方法可以创建一个生成器，用以生成所要查找的目录及其子目录下的所有文件。
根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】
2. os.path.join(path1[, path2[, ...]])，把目录和文件名合成一个路径
3. 查找指定文件后缀名的文件
'''
'''
1. Button: 按钮
2. Label： 标签，可以显示文字或图片；
3. place, 组件可以直接使用坐标来放置组件
4. command, 指定按钮消息的回调函数
5. tk.Text, 文本框
6. selectforeground，选定文本前景色

7. win主机上的绝对路径用 \\
'''

def get_filelist(source_dir):

    # home,dirs,files= 文件夹路径, 文件夹名字, 文件名
    for home, dirs, files in os.walk(source_dir):
        print("----------------------dir list-------------------")
        for source_dir in dirs:
            print("文件夹路径：",source_dir)

        print("---------------------file list-------------------")

        for filename in files:
            print("文件名是：",filename)
            fullname = os.path.join(home, filename)
            print("文件路径是：",fullname)
            readpath.append(fullname)


    # 判断后缀名为mp3的文件路径
    for i in range(len(readpath)):
        if readpath[i].split(".")[-1] == "mp3":
            print("------------------------------------------------")
            print("------------------------------------------------")
            print("后缀名为mp3的文件路径名为：", readpath[i])
            list_path.append(readpath[i])
    return list_path

def save_path(list_path):
    f = open('path.txt', 'w', encoding='utf-8')  # a+表示追加，w的话会覆盖
    for i in range(len(list_path)):
        f.write(f"{list_path[i]}\n")

def read_path():
    f = open('path.txt', 'r', encoding='utf-8')
    list_a = f.readlines()
    for index in range(len(list_a)):     #如果不遍历输出列表，格式输出的很难看
        # print(list_a[index])             #测试读操作正常后，就不需要打印了
        t.insert('insert', f'{list_a[index]}\n')  # 插入到tkinter界面




if __name__ == "__main__":
    # 用于接收所有的文件路径
    readpath = []
    # 用于最终接收查找后得到的路径
    list_path = []

    get_filelist('C:')
    get_filelist('D:')
    get_filelist('E:')

    save_path(list_path)



    # 设置窗口title和 大小
    win = tk.Tk()
    win.title('查找后缀mp3的路径')
    win.geometry('600x600')
    # Entry 单行文本
    L = tk.Label(win, bg="yellow", text="查找后缀mp3的路径", font=("KaiTi", 26), width=36, height=3)  # 生成标签，   font：字体
    L.place(x=0, y=0)
    # 设置随机点名按钮 退出系统按钮
    b1 = tk.Button(win, bg='red', text="查找路径", width=25, height=2, command=read_path)  # command,指定按钮消息的回调函数
    b1.place(x=80, y=200)
    b2 = tk.Button(win, bg='red', text="退出系统", width=25, height=2, command=win.quit)
    b2.place(x=325, y=200)
    # Entry 单行文本
    L = tk.Label(win, text="查找后缀mp3的路径如下", font=("KaiTi", 18), width=36, height=1)
    L.place(x=90, y=315)
    # 设置多行文本框  宽 高  文本框中字体  选中文字时文字的颜色
    t = tk.Text(win, width=36, height=8, font=("KaiTi", 24), bg='green', selectforeground='green')  # 显示多行文本
    t.place(x=10, y=350)
    win.mainloop()  # 进入消息循环（必需组件）
