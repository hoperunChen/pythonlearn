#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#dbHelper
import sqlite3

class DbHelper(object):
	def __init__(self, path):
		super(DbHelper, self).__init__()
		self.path = path
		self.conn = None


	def getConn(self):
		self.conn = sqlite3.connect(self.path)
		return self.conn.cursor()

	def close(self,cursor):
		cursor.close()
		self.conn.commit()
		self.conn.close()

	def queryAll(self,tableName):
		sql = "select * from %s "%(tableName)
		cursor = self.getConn()
		cursor.execute(sql)
		values = cursor.fetchall()
		self.close(cursor)
		return values


if __name__  == '__main__':
	cf = DbHelper("test.db")
	values = cf.queryAll('TEST_TABLE')
	for id,name in values:
		print id + "-->" + name

