# -*- coding: UTF-8 -*-
'''
1. Button: 按钮
2. Label： 标签，可以显示文字或图片；
3. place, 组件可以直接使用坐标来放置组件
4. command, 指定按钮消息的回调函数
5. tk.Text, 文本框
6. selectforeground，选定文本前景色

7. win主机上的绝对路径用 \\
'''
import tkinter as tk
# from pandas import read_excel
import pandas as pd
from random import randint


# 读取数据
df1 = list(pd.read_excel('D:\\联电\\python\\easygui, tkinter\\tkinter\\学生名单_test.xlsx')['姓名'])
# print(df1)
df2 = list(pd.read_excel('D:\\联电\\python\\easygui, tkinter\\tkinter\\学生名单_test.xlsx')['性别'])

# 点名
def roll_call():
    index_ = randint(0, len(df1) - 1)        # 产生随机索引
    name = df1.pop(index_)                   # 弹出随机索引对应的姓名
    sex = df2.pop(index_)                    # 弹出随机索引对应的性别
    t.insert('insert', f'{name}  {sex}\n')   # 插入到tkinter界面

# 设置窗口title和 大小
win = tk.Tk()
win.title('随机点名系统')
win.geometry('600x600')

# Entry 单行文本
L = tk.Label(win, bg="yellow", text="随机点名系统", font=("KaiTi", 26), width=36, height=3)   # 生成标签，   font：字体
L.place(x=0, y=0)

# 设置随机点名按钮 退出系统按钮
b1 = tk.Button(win, bg='red', text="随机点名", width=25, height=2, command=roll_call)  # command,指定按钮消息的回调函数
b1.place(x=80, y=200)
b2 = tk.Button(win, bg='red', text="退出系统", width=25, height=2, command=win.quit)
b2.place(x=325, y=200)

# Entry 单行文本
L = tk.Label(win, text="点到的学生名单如下", font=("KaiTi", 18), width=36, height=1)
L.place(x=90, y=315)

# 设置多行文本框  宽 高  文本框中字体  选中文字时文字的颜色
t = tk.Text(win, width=36, height=8, font=("KaiTi", 24), bg='green',selectforeground='green')  # 显示多行文本
t.place(x=10, y=350)

win.mainloop()  #进入消息循环（必需组件）