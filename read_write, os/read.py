import os
#f = open('register.txt', 'r', encoding='utf-8')
#msgList = [i for i in f.readlines()]
#for num in range(0, len(msgList)):
#  print(msgList[num])


f = open('1.json', 'r', encoding='utf-8')
list_a = f.readlines() #读取所有行包括"\n"字符并返回列表
#print(list_a)         #如果不遍历输出列表，格式输出的很难看
for index in range(len(list_a)):
    print(list_a[index])  #测试读操作正常后，就不需要打印了


print (f)
