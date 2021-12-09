from kafka import KafkaProducer
'''
1. 如果是测试，需要推送的消息数比较小，那么需要增大循环次数，可设置5000次
2. 如果使用pycharm,那么需要在本地windows主机hosts文件内，增加topic的partition所落到节点的ip信息
3. 为了解决1的问题，需要增加producer.flush()，producer.close()

'''
#------------------------------------------第一种方法--------------------------------------------------------
producer= KafkaProducer(bootstrap_servers='')

for i in range(5000):
    producer.send("test4", bytes('1ddddddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaa', 'utf-8'))
    
    
    
#------------------------------------------更好的办法--------------------------------------------------------
producer= KafkaProducer(bootstrap_servers='')

for i in range(5):
    producer.send("test4", bytes('1ddddddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaa', 'utf-8'))
producer.flush()
producer.close()