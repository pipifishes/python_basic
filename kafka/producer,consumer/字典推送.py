#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kafka import KafkaProducer
import json

'''
value_serializer=str.encode,序列化： 对下面这种字典格式加这个参数很重要，否则会报错：assert type(value_bytes) in (bytes, bytearray, memoryview, type(None))
错误原因：send函数的value_bytes是str类型

'''

# KAFKA生产者对象创建
producer = KafkaProducer(bootstrap_servers="",value_serializer=str.encode)

problem_message = [
	{"function":"uaes-iot-power-guard","message":{"timeHapRec":"2021-09-13 16:35:00","silenceFlag":"Y","displayFlag":"1","pCode":"P000A00","vin":"TESTCHB0710000001","gps":{"lon":"","lat":""},"title":"进气VVT存在故障隐患","faultLevel":"1","timehealRec":""}},
	{"function":"uaes-iot-power-guard","message":{"timeHapRec":"2021-09-13 16:35:00","silenceFlag":"Y","displayFlag":"1","pCode":"P000A00","vin":"TESTCHB0710000001","gps":{"lon":"","lat":""},"title":"进气VVT故障","faultLevel":"2","timehealRec":""}},
	{"function":"uaes-iot-power-guard","message":{"timeHapRec":"2021-09-13 16:35:00","silenceFlag":"Y","displayFlag":"1","pCode":"P000A00","vin":"TESTCHB0710000001","gps":{"lon":"","lat":""},"title":"进气VVT恢复正常","faultLevel":"0","timehealRec":"2021-09-13 16:45:27"}}
]

# 消费消息并转发
for message in problem_message:
    print(message)
    producer.send("maintenance", json.dumps(message), partition=0) # 把上面的字典格式转成字符串格式
 
producer.flush()
producer.close()
