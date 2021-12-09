#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
BAIC-dev-Kafka
用json的原因是，拿到的txt文本原始数据，就是json的格式

'''

import re
import json
import pymysql
import time

from kafka import KafkaProducer
from kafka.errors import KafkaError

# producer = KafkaProducer(bootstrap_servers='')
# topic = 'GWMCANDATA'

def readMsg():
   f = open('1.json', 'r', encoding='utf-8')
   list_a = f.readlines() #读取所有行包括"\n"字符并返回列表
   #print(list_a)         #如果不遍历输出列表，格式输出的很难看
   for index in range(len(list_a)):
       #print(list_a[index])  #测试读操作正常后，就不需要打印了
       dealKafka(list_a[index])  #调用函数，把list_a传入下一个函数
      

def dealKafka(L):
   msglist = re.findall(r'{.*}',f'{L}') #正则，获取上面的list_a，并贪婪匹配给msglist
   #print(msglist)


   for i in range(len(msglist)):
      msglistDic = eval(msglist[i])  # eval，转化为字典
   # 获取字典中的VIN值的列表
      if "value" in msglistDic.keys():  # 调用字典中的keys()方法
         valuelist = msglistDic["value"]
         print(valuelist)
  
if __name__ == '__main__':
   
   readMsg()
   producer.close() #关闭kafka发送
   print('done')     
