from  kafka import KafkaConsumer
#消费kafka中最新的数据 并且自动提交offsets[消息的偏移量]
#先把消费的脚本开着，然后再运行推送的脚本    ，不然消费脚本会被hang住

consumer = KafkaConsumer('',group_id='',bootstrap_servers=[''],auto_offset_reset='latest')

for msg in consumer:
    # msg.value读取kafka的消息,bytes输出
    kafka_message=str(msg.value)
    print(kafka_message)