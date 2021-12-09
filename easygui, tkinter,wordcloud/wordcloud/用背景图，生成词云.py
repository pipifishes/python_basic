#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba # 负责分词功能
import  wordcloud # 负责生成词云图
import matplotlib # 负责设置颜色

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
'''
用上了背景图制作词云
'''

# 打开文件 -> 实例化 WordCloud 类 -> 调用 generate() 方法并传入文本o
file = open("./最多弹幕.txt","r" ,encoding="utf-8")
text = file.read()
# 初始化自定义背景图片
bg = Image.open("./20190929023034312.png")
graph = np.array(bg)
# 还需要筛选，去除一些不相干的关键字，wordcloud 里面有一个 stopwords 参数，它可以指定一个由字符串构成的集合：
stopwords = {"野生技术协会", "编程", "教育", "讲座", "科技", "语言", "技术宅", "面试", "自学", "原创", "公开课", "程序员", "学习", "课程", "教程", "计算机", "线上课堂", "视频教程"}
wc = wordcloud.WordCloud(font_path=r"C:\Windows\Fonts\simhei.ttf",stopwords=stopwords,background_color='white',mask=graph,height=600,width=800)   # 找到本机所用的字体集
res = wc.generate(text)
print(res)
# 绘制文字的颜色以背景图颜色为参考
bg_color = wordcloud.ImageColorGenerator(graph)
wc.recolor(color_func=bg_color)
wc.to_file("./wordcloud.png")  # 本地生成图片
# 显示图片
plt.figure("词云图")   #指定所绘图名称
plt.imshow(wc)         # 以图片的形式显示词云
plt.axis("off")       # 关闭图像坐标系
plt.show()
