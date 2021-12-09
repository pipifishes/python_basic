from  kafka import KafkaConsumer
#消费kafka中最新的数据 并且自动提交offsets[消息的偏移量]

consumer = KafkaConsumer('',group_id='',bootstrap_servers=[''],auto_offset_reset='latest')

for msg in consumer:
    # msg.value读取kafka的消息,bytes输出
    kafka_message=str(msg.value)
    # print(kafka_message)

    # 把msg中字段stype为gpfTemp的信息筛选出来
    if "gpfTemp" in kafka_message:
        print(kafka_message)