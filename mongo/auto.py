#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import datetime
import os
import time
import datetime
import codecs
import csv
from pymongo import MongoClient
import math
from ks3.connection import Connection
from filechunkio import FileChunkIO



now = datetime.datetime.now()

print( now.strftime("%Y-%m-%d") ) #当前时间 2020-11-25

#获得1天的时间
lastTwoDay = now - datetime.timedelta(days=2)
lastOneDay = now - datetime.timedelta(days=1)
#获取7天的时间
lastSevenDay = now - datetime.timedelta(days=5)
lastSixDay = now - datetime.timedelta(days=4)

#只显示年月日
TwoDay=lastTwoDay.strftime("%Y-%m-%d")
OneDay=lastOneDay.strftime("%Y-%m-%d")
SevenDay=lastSevenDay.strftime("%Y-%m-%d")
SixDay=lastSixDay.strftime("%Y-%m-%d")

#获取整点时间 x-x-x:00:00:00
t_str_begin = str(TwoDay)+" 00:00:00"
t_str_end = str(OneDay)+" 00:00:00"
t_str_begin_bk = str(SevenDay)+" 00:00:00"
t_str_end_bk = str(SixDay)+" 00:00:00"

print (TwoDay)  #数据保留两天
print (OneDay)
print (t_str_begin) #两天前的时间 2020-11-23 00:00:00
print (t_str_end) #一天前的时间 2020-11-23 00:00:00


#把获取的时间转换为时间戳
bt=time.strptime(t_str_begin,'%Y-%m-%d %H:%M:%S')
bttime = int(time.mktime(bt))*1000
et=time.strptime(t_str_end,'%Y-%m-%d %H:%M:%S')
ettime = int(time.mktime(et))*1000

bt_bk=time.strptime(t_str_begin_bk,'%Y-%m-%d %H:%M:%S')
bttime_bk = int(time.mktime(bt_bk))*1000
et_bk=time.strptime(t_str_end_bk,'%Y-%m-%d %H:%M:%S')
ettime_bk = int(time.mktime(et_bk))*1000

print (bttime)
print (ettime)
print (bttime_bk)
print (ettime_bk)



#设两个集合，a是mongo中的原表，b是7天备份的表
list_a = ["gwm_b01_can_data","gwm_b01_gps_data","gwm_b01_tsp_data",
"gwm_b06_can_data","gwm_b06_gps_data","gwm_b06_tsp_data",
"gwm_chb071_can_data","gwm_chb071_gps_data",
"gwm_chb071_tsp_data","gwm_chb121v_2021_can_data","gwm_chb121v_2021_gps_data","gwm_chb121v_2021_tsp_data","gwm_chb131_2021_can_data","gwm_chb131_2021_gps_data","gwm_chb131_2021_tsp_data"]
list_b = ["gwm_b01_can_data","gwm_b01_gps_data","gwm_b01_tsp_data",
"gwm_b06_can_data","gwm_b06_gps_data","gwm_b06_tsp_data",
"gwm_chb071_can_data","gwm_chb071_gps_data",
"gwm_chb071_tsp_data","gwm_chb121v_2021_can_data","gwm_chb121v_2021_gps_data","gwm_chb121v_2021_tsp_data","gwm_chb131_2021_can_data","gwm_chb131_2021_gps_data","gwm_chb131_2021_tsp_data"]


# Connect to kS3
ak = ''
sk = ''
c = Connection(ak, sk, host='', is_secure=False, domain_mode=False)
bucket_name = ""
b = c.get_bucket(bucket_name)

#Connect to raw_data
client = MongoClient('',27017)
client.raw_data.authenticate("raw_data","raw_data",mechanism='SCRAM-SHA-1')
db=client.raw_data
#Connect to raw_data_bk
client1 = MongoClient('',27017)
client1.raw_data_bk.authenticate("raw_data","raw_data",mechanism='SCRAM-SHA-1')
db1=client1.raw_data_bk

#for循环，遍历15张原表
for index in range(len(list_a)):
   #print (list_a[index])
   fileName = str(list_a[index])+str(TwoDay)+".json"
   #print (fileName)
   
   def mongoet():
      
      # 连接数据库--》shell方式，dump数据到/mnt/mongo下，并上传该数据到新库新表中
      durtime = f'{{"ts":{{$gte:"{bttime}",$lt:"{ettime}"}}}}'
      host = ""
      mongoexport = f"/usr/local/mongodb/mongodb-linux-x86_64-4.0.7/bin/mongoexport -h {host} --port 27017 -u  -p  -d  -c {list_a[index]} -q '{durtime}' -o /backup/{fileName}"
      print(mongoexport)
      val = os.system(mongoexport)
      print("dump数据到/backup下")
      print("--------------------------------------------------------------------------")
      #print(val)
       
      # 把上述mongoexportdump的数据，导入到7天备份表中
      mongoimport = f"/usr/local/mongodb/mongodb-linux-x86_64-4.0.7/bin/mongoimport -h {host}  -u  -p  -d -c {list_b[index]} --file /backup/{fileName} --authenticationDatabase admin"
      #print(mongoimport)
      val = os.system(mongoimport)
      #print(val)
      print("上传export的数据到新库新表中")
      print("--------------------------------------------------------------------------")
     
   mongoet()
   
   #删除原表中的2天前的数据
   # 连接数据库
   collection=db[f'{list_a[index]}']
   myquery={"ts":{"$gte":f"{bttime}","$lt":f"{ettime}"}}
   if myquery:
      data = collection.delete_many(myquery)
      print(data.deleted_count,"条数据在mongo中已删除")
   else:
      print("该表该天没有数据")
   print("----------------------------------------------------------------------------")

   #删除备份表中的7天前的数据
   # 连接数据库
   collection1=db1[f'{list_b[index]}']
   myquery1={"ts":{"$gte":f"{bttime_bk}","$lt":f"{ettime_bk}"}}
   if myquery1:
      data1 = collection1.delete_many(myquery1)
      print(data1.deleted_count,"条数据在mongo中已删除")
   else:
      print("该备份表7天前没有数据")
   print("-------------------------------")
   


   # Connect to ks3,分片上传
   source_path = f'/backup/{fileName}'
   print(source_path)
   source_size = os.stat(source_path).st_size

   #Create a multipart upload request
   # 此处os.path.basename(source_path)可以替换为需要设置的objectKey,是ks3的路径
   mp =b.initiate_multipart_upload(f"mongo/raw_data/{list_a[index]}/{fileName}", policy="private")
   print(mp)
   # Use a chunk size of 50 MiB (feel free to change this)
   chunk_size = 70428800
   chunk_count = int(math.ceil(source_size*1.0 / chunk_size*1.0))
   # Send the file parts, using FileChunkIO to create a file-like object
   # that points to a certain byte range within the original file. We
   # set bytes to never exceed the original file size.
   if chunk_count == 0:
      print("该表该天未获得数据,上传部分结束")
   else:
      for i in range(chunk_count):
         offset = chunk_size * i
         bytes = min(chunk_size, source_size - offset)
         with FileChunkIO(source_path, 'r', offset=offset, bytes=bytes) as fp:
            mp.upload_part_from_file(fp, part_num=i + 1)
      ret = mp.complete_upload()
      if ret and ret.status == 200:
         print("分片上传到ks3上成功")
         print("该表该天的数据已上传完成")
         print("-------------------------------")


#关闭两个连接
client.close()
client1.close()

print("程序开始的时间",now)
now1 = datetime.datetime.now()
print("程序结束的时间",now1)

