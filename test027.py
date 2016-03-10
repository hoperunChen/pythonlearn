#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#sqlite
import sqlite3

values = ""
conn = None
cursor = None
try:
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
	cursor.execute('select * from user')
	values = cursor.fetchall()
	
except Exception, e:
	raise e
finally:
	cursor.close()
	conn.commit()
	conn.close()


print values