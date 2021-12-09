from kafka import KafkaProducer
'''
1. 如果是测试，需要推送的消息数比较小，那么需要增大循环次数，可设置5000次
2. 如果使用pycharm,那么需要在本地windows主机hosts文件内，增加topic的partition所落到节点的ip信息， 发现阿里云不需要，金山云需要



'''
producer= KafkaProducer(bootstrap_servers='')

for i in range(5000):
    producer.send("UAES-GEELY-NEV-DATA-TOPIC", bytes('14524', 'utf-8'))

producer.flush()
producer.close()