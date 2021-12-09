#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
先读一个文件 ，再把读到的内容存到另一个文件中
'''
import os


def read():
    #读文件
    f = open('flink.txt', 'r', encoding='utf-8')
    list_a = f.readlines()               #读取所有行包括"\n"字符并返回列表
    #print(list_a)
    for index in range(len(list_a)):     #如果不遍历输出列表，格式输出的很难看
        #print(list_a[index])             #测试读操作正常后，就不需要打印了
        write(list_a[index])

def write(L):
    #写（保存）文件
    f = open('filnk_copy.txt','a+',encoding='utf-8')     #a+表示追加，w的话会覆盖
    f.write(f"{L}")


if __name__ == '__main__':
    read()
    print("done")

