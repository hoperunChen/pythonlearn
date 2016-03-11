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

	def executeQuery(self,sql):
		print sql
		cursor = self.getConn()
		cursor.execute(sql)
		values = cursor.fetchall()
		self.close(cursor)
		return values


	def queryAll(self,tableName):
		sql = "select * from %s "%(tableName)
		values = self.executeQuery(sql)
		return values

	def query(self,fieldsName,tableName):
		sql = "select "
		sql = sql + self.generateFieldsSql(fieldsName)
		sql = sql + "from %s "%(tableName)
		values = self.executeQuery(sql)
		return values

	def generateFieldsSql(self,fieldsName):
		fieldSql = "";
		for i,field in enumerate(fieldsName):
			fieldSql = fieldSql + field
			if i < len(fieldsName) - 1:
				fieldSql = fieldSql + ","
			else :
				fieldSql = fieldSql + " "
		return fieldSql



if __name__  == '__main__':
	cf = DbHelper("test.db")
	#values = cf.queryAll('TEST_TABLE')
	values = cf.query(['id'],'TEST_TABLE')
	for id in values:
		print id 

