from  kafka import KafkaConsumer
import json
‘’‘
消费kafka中最新的数据 并且自动提交offsets[消息的偏移量]
group_id,可以不用写，有默认的
’‘’
consumer = KafkaConsumer('',group_id='',bootstrap_servers=[''],auto_offset_reset='latest')
for msg in consumer:
    # msg.value读取kafka的消息,bytes输出
    kafka_message=str(msg.value)
    #print(kafka_message)
    if "gpfTemp" in kafka_message:
        #print(kafka_message)
        if "LNBFCUKK6LT100231" in kafka_message:
            if "2021-05-13" in kafka_message: 
                print(kafka_message)
                f = open("./kafka_message.txt","a")
                #f.write(kafka_message)
                f.write("{}\n".format(kafka_message))
