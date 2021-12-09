from  kafka import KafkaConsumer
#消费kafka中最新的数据 并且自动提交offsets[消息的偏移量]
consumer = KafkaConsumer('',bootstrap_servers=[''],auto_offset_reset='earliest')
for msg in consumer:
	kafka_message=str(msg.value)
    # print(kafka_message)
	if "LGWEF6A50LH250093" in kafka_message:
		if "1617415645317" in kafka_message:
			print(kafka_message)
			with open(r"./message.txt",'a') as f:
			    f.write("{}\n".format(kafka_message))










