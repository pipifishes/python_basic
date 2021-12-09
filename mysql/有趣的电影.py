#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
1.创建 cinema表，编写一个 SQL 查询，找出所有影片描述为非 boring (不无聊) 的并且 id 为奇数 的影片，结果请按等级rating 排列
2.连接的是linux自建的数据库，需要注意的是，需要mysql授权root用户访问
'''
import pymysql
#打开数据库连接
conn = pymysql.connect(host='', port=3306, user='', passwd='', charset='utf8')
conn.select_db('test3')
#获取游标
cursor=conn.cursor()

# 创建cinema表
cursor.execute('drop table if exists cinema')
sql1="""CREATE TABLE IF NOT EXISTS `cinema` (
	  `id` int(11) NOT NULL AUTO_INCREMENT,
	  `movie` varchar(255) NOT NULL,
	  `description` varchar(255) NOT NULL,
	  `rating` float,
	  PRIMARY KEY (`id`)
	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=0"""
# 使用execute方法执行SQL语句,创建user表
cursor.execute(sql1)

# 插入数据的方式，通过字符串传入值
sql2= "insert into cinema values(%s,%s,%s,%s)"
insert= cursor.executemany(sql2,[(1,'war','great 3D',8.9),(2,'Science','fiction',8.5),(3,'irish','boring',6.2),(4,'Ice song','Fantacy',8.6),(5,'House card','Interesting',9.1)])
print ('批量插入返回受影响的行数：',insert)


# 查看新创建的表
cursor.execute('select * from cinema')
res=cursor.fetchall()
print (res) #输出内容

# 输出符合条件的影片
sql3 = "select * from cinema where description != 'boring' and id%2 != 0 order by rating desc ;"
cursor.execute(sql3)
val = cursor.fetchall()
print(val)



cursor.close()#先关闭游标
conn.commit()
conn.close()#再关闭数据库连接

