#！/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import easygui as g
#对于大部分的EasyGui函数都有默认参数，几乎所有的组件都会显示一个消息和标题。
#标题默认是空字符串，信息通畅有一个简单的默认值
#比如msgbox()函数标题部分的参数就是可选的，所以你调用msgbox的时候可以指定一个消息参数，例如：
msg = g.msgbox("Hello Easy GUI")
#当然你也可以指定信息参数和标题参数
title = g.msgbox(msg="我一定要学会编程！",title="标题部分",ok_button="加油")

# ccbox(),选择框
if g.ccbox("亲爱的还玩吗?",choices=("还要玩！","算了吧")):
    g.msgbox("还是不玩了，快睡觉吧！")
else:
    sys.exit(0)

# buttombox()，定义自己的一组按钮
g.buttonbox(msg="你喜欢下面哪种水果?",title="",choices=("西瓜","苹果","草莓"))
# 在buttonbox()中显示图片,仅支持 GIF 格式
g.buttonbox(msg="大家说chouchou可爱吗?",image="22.gif",choices=("可爱","不可爱","财迷"))

# choicebox()，多个选择框，只能选一项
msg = "选择你喜欢的一种业余生活"
title = ""
choicess_list = ["看书","游泳","骑自行车","玩游戏"]
reply = g.choicebox(msg,choices=choicess_list)

# multchoicebox()，多个选择框，支持用户选择 0 个，1 个或者同时选择多个选项
g.multchoicebox(msg="请选择你爱吃哪些水果?",title="",choices=("西瓜","香蕉","苹果","梨"))

# enterbox()，用户提供一个最简单的输入框
g.enterbox(msg="请说出此时你的心里话",title="心里悄悄话")

# integerbox()，为用户提供一个简单的输入框，用户只能输入范围内（lowerbound参数设置最小值，upperbound参数设置最大值）的整型数值，否则会要求用户重新输入
g.integerbox(msg="请输入您的得分",title="分数计",lowerbound=0,upperbound=100)

# mulenterbox()，用户提供多个简单的输入框
msg = "请填写一下信息(其中带*号的项为必填项)"
title = "账号中心"
fieldNames = ["*用户名","*真实姓名","固定电话","*手机号码","QQ","*Email"]
fieldValues = []
fieldValues = g.multenterbox(msg,title,fieldNames)
#print(fieldValues)
while True:
    if fieldValues == None :
        break
    errmsg = ""
    for i in range(len(fieldNames)):
        if fieldValues[i] == "" and fieldValues[i][0] == "*":
            errmsg += ("【%s】为必填项   " %fieldNames[i])
    if errmsg == "":
        break
    fieldValues = g.multenterbox(errmsg,title,fieldNames,fieldValues)
print("您填写的资料如下:%s" %str(fieldValues))

# passwordbox(),跟 enterbox() 样式一样，不同的是用户输入的内容用"*"显示出来，返回用户输入的字符串
msg = "请输入你的密码"
user_password = g.passwordbox(msg)
print(str(user_password))

# multpasswordbox(),最后一个输入框显示为密码的形式（"*"）
msg = "请输入用户名和密码"
title = "用户登录接口"
user_info = []
user_info = g.multpasswordbox(msg,title,("用户名","密码"))
print(user_info)