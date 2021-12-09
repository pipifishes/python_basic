from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='',acks=0,batch_size=1048576,retries=0,buffer_memory=335544320,max_request_size=10048576)
parse = open("/mnt/liujinhe/parse.txt","r")
test=parse.read()
a=test.split("\n")
while 0==0:
    for i in range(len(a)):
        producer.send("",bytes(str(a[i]),'utf-8'))
