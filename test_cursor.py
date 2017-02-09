#! /usr/bin/env python3
# coding:utf-8

from mysql.connector import connect

db_config = {
	'host':'localhost',
	'port':3306,
	'user':'root',
	'passwd':'zhuanke',
	'db':'mysql',

}

conn = connect(**db_config)
cur = conn.cursor()
cur.execute('Select Host,User, authentication_string From user')

print('Mysql执行查询成功！')

for i in cur:
	print(i)



