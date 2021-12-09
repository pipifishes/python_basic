#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
1. 如果是测试，需要推送的消息数比较小，那么需要增大循环次数，可设置5000次
2. 如果使用pycharm,那么需要在本地windows主机hosts文件内，增加topic的partition所落到节点的ip信息
"""

import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

producer= KafkaProducer(bootstrap_servers='')
topic = 'test4'
dic = {"name":"zzz","bir":"19990101"}
# 将python对象编码成Json字符串
msg = json.dumps(dic)


for i in range(5000):
    producer.send(topic, bytes(str(msg),'utf-8'))
    
producer.flush()
producer.close()

