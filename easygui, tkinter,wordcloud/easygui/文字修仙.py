#！/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import easygui as g
g.msgbox(msg="Welcome to the world of writing！",title="topic",ok_button="come on")
g.buttonbox(msg="Select an School", image="22.gif",choices=("Falling flowers","Purple thunder","flying sword"))

# multpasswordbox(),最后一个输入框显示为密码的形式（"*"）
msg = "please input user and number"
title = "User login interface"
user_info = []
user_info = g.multpasswordbox(msg,title,("user","number"))
# print(user_info)

g.msgbox("You have joined the sect")

# multchoicebox()，多个选择框，支持用户选择 0 个，1 个或者同时选择多个选项
g.multchoicebox(msg="Secret place",title="",choices=("medicinal powder","Magic weapon","Gongfa"))