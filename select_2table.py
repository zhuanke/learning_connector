#! /usr/bin/env python3
# coding:utf-8

from mysql.connector import connect

db_config = {
	'host':'localhost',
	'port':3306,
	'user':'root',
	'passwd':'zhuanke',
	'db':'mydb02',

}

conn = connect(**db_config)
cur = conn.cursor()

sql = '''
SELECT * FROM `student`
'''

sql2 = '''
SELECT * FROM `teacher`
'''

feedback = cur.execute(sql)
res1 = [i for i in cur]

feedback2 = cur.execute(sql2)
res2 = [i for i in cur]


for i in res1:
	print(type(i))
	print(i)

for i in res2:
	print(type(i))
	print(i)
print('Mysql执行查询成功！',feedback,feedback2)



