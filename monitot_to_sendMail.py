#!/usr/bin/python3
import pymysql
 
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def search_mysql():
  
   sql="select * from user;"
   cur.execute(sql)
   res=cur.fetchall()
   print (res) 
   print('共%d条数据'%len(res)) 
   return res  

def sendMail(L): 
   my_sender=''    # 发件人邮箱账号
   my_pass = ''    # 发件人邮箱密码(当时申请smtp给的口令)
   my_user=''      # 收件人邮箱账号，我这边发送给自己
   ret=True
   
   try:
      msg=MIMEText(f'{L}','plain','utf-8')
      msg['From']=formataddr(["",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
      msg['To']=formataddr(["",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
      msg['Subject']="北汽内网kafka"                # 邮件的主题，也可以说是标题
 
      server=smtplib.SMTP_SSL("", 465)  # 发件人邮箱中的SMTP服务器，端口是25
      server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
      server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
      server.quit()  # 关闭连接
   except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
         ret=False
   return ret
 


if __name__ == '__main__':
   print('begin')
   #打开数据库连接
   conn = pymysql.connect(host='', port=3306, user='', passwd='', charset='utf8')
   #打开数据库连接
   conn.select_db('')
   #获取游标
   cur=conn.cursor()
 
   
   file_content= search_mysql()
   sendMail(file_content)

   cur.close()
   conn.commit()
   conn.close()
   print('sql执行成功')
    
