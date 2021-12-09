#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
查询车辆是否落库
原文本是txt格式
'''


import json
import pymysql

# 获取文本中某两个值
def txtDeal():
    f = open('1.txt', 'r', encoding='utf-8-sig')
    data = [i for i in f.readlines()]
    # 新列表用来接收 vin,timestamp
    list_timestamp = []
    list_vin = []
    # 新字符串用来接收 拼接后的string  --> 到}结束
    jsonIn = ''
    for num in range(0, len(data)):
        if str(data[num]).strip() != '}':
            jsonIn = jsonIn + str(data[num]).strip()
            # print(jsonIn) # 用来查看，读每一行然后拼接起来的结果
        else:
            jsonIn = jsonIn + str(data[num]).strip()
            jsonOut = json.loads(jsonIn,strict=False)   # 已经读到了一个json的最后}
            # print(jsonOut)
            # print('timestamp is :',jsonOut['timestamp'])
            # print('vin is :', jsonOut['vin'])
            jsonIn = ''

            list_vin.append(jsonOut['vin'])
            list_timestamp.append(str(jsonOut['timestamp']).split(".")[0])  # 2021-07-01 13:54:40.000 --> 2021-07-01 13:54:40
    print(list_timestamp)
    print(list_vin)
    list_union(list_vin,list_timestamp)

# zip联合两个列表
def list_union(list1,list2):
    newdata = zip(list1,list2)
    data_list =list(newdata)
    print(data_list)
    deal_sql(data_list)

# 查询mysql
def deal_sql(data_list):
    for i in range(len(data_list)):
        conn = pymysql.connect(host='', port=3306, user='', passwd='', charset='utf8')
        conn.select_db('uaes_iot_maintenance_secretary')
        cur = conn.cursor()
        cur.execute(f"select vin,create_datetime from uaes_iot_maintenance_secretary.gwm_maintenance_evt where vin = '{data_list[i][0]}' and timestamp = '{data_list[i][1]}';")
        # 取所有数据
        res = cur.fetchall()
        print(res)  # 输出内容

        cur.close()
        conn.commit()
        conn.close()

if __name__ == '__main__':
    txtDeal()