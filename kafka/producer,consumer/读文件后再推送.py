from kafka import KafkaProducer
import os

producer = KafkaProducer(bootstrap_servers='')

f = open("parse.txt","r")
list_a = f.readlines()
#print(type(test))

for i in range(len(list_a)):
    print(i,list_a[i])
    producer.send("test4", bytes(str(list_a[i]), 'utf-8'))
