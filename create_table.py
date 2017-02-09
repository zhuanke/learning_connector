#! /usr/bin/env python3
# coding:utf-8

from mysql.connector import connect

db_config = {
	'host':'localhost',
	'port':3306,
	'user':'root',
	'passwd':'zhuanke',
	'db':'mydb01',

}

conn = connect(**db_config)
cur = conn.cursor()
sql = '''
CREATE TABLE `from_connector`(
 `id` int PRIMARY KEY auto_increment,
 `name` varchar(20) NOT NULL
)
'''
feedback = cur.execute(sql)

print('Mysql执行查询成功！',feedback)

for i in cur:
	print(i)



