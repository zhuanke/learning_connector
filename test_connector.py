#! /usr/bin/env python3
# coding:utf-8
print(r"it's my first github")

from mysql.connector import connect
print('导入成功！')

db_config = {
	'host':'localhost',
	'port':3306,
	'user':'root',
	'passwd':'zhuanke',
	'db':'mydb01',
}


conn = connect(**db_config)
print('连接MySQL数据库成功')
