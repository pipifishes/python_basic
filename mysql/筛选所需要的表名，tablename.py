#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import os

'''
查看mysql所有表名带’copy‘字段的
'''
# 列举库名
list = ['uaes_burypoint','uaes_iot_battery','uaes_iot_car_admin','uaes_iot_driving_talent','uaes_iot_driving_talent_test','uaes_iot_emr','uaes_iot_energy_consumption','uaes_iot_fuel_consumption','uaes_iot_fuel_fill','uaes_iot_gas_station','uaes_iot_home_company','uaes_iot_maintenance_secretary','uaes_iot_power_guard','uaes_iot_public_service','uaes_iot_service_shop','uaes-rqms-charging-monitor','uaes-rqms-common-service','uaes-rqms-component-lifecycleinfo','uaes-rqms-datalogger','uaes-rqms-opload-analysis','uaes-rqms-power-guard']
for index in range(len(list)):
    #打开数据库连接
    conn = pymysql.connect(host='', port=3306, user='', passwd='', charset='utf8')
    conn.select_db(f'{list[index]}')
    print("database is ",f'{list[index]}')
    #获取游标
    cur=conn.cursor()

    cur.execute("show tables like '%copy%';")

    #取所有数据
    res=cur.fetchall()
    print (res) #输出内容
    #print (type(res))
    #print('共%d条数据'%len(res)) #输出条数
    print('-'*150)

    # # write() argument must be str, not tuple
    # f = open ('tablename.txt','a+',encoding ='utf-8')
    # f.write(str(res))


cur.close()
conn.commit()
conn.close()
print('sql执行成功')

