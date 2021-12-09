#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba # 负责分词功能
import  wordcloud # 负责生成词云图
import matplotlib # 负责设置颜色
# import opencv-python # 负责设置词云图蒙版

# 打开文件 -> 实例化 WordCloud 类 -> 调用 generate() 方法并传入文本o
file = open("./最多弹幕.txt","r" ,encoding="utf-8")
text = file.read()
# 还需要筛选，去除一些不相干的关键字，wordcloud 里面有一个 stopwords 参数，它可以指定一个由字符串构成的集合：
stopwords = {"野生技术协会", "编程", "教育", "讲座", "编程技术宅", "教学", "电脑", "技术", "编程教育", "编程入门", "开发", "科学", "演示", "软件", "编程视频教程", "编程课程", "教学视频", "经验分享", "IT", "编程语言", "编程学习", "互联网", "考试", "考研", "科技", "语言", "技术宅", "面试", "自学", "原创", "公开课", "程序员", "学习", "课程", "教程", "计算机", "线上课堂", "视频教程"}
wc = wordcloud.WordCloud(font_path=r"C:\Windows\Fonts\simhei.ttf",stopwords=stopwords,background_color='black',height=800,width=1000)   # 找到本机所用的字体集
res = wc.generate(text)
print(res)

# 展示的话可以使用 pillow 模块实现，调用 to_image() 方法
image = wc.to_image()
image.show()

