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
		self.conn.text_factory = str
		return self.conn.cursor()

	def close(self,cursor):
		cursor.close()
		self.conn.commit()
		self.conn.close()

	def generateFieldsSql(self,fieldsName):
		fieldSql = "";
		for i,field in enumerate(fieldsName):
			fieldSql = fieldSql + field
			if i < len(fieldsName) - 1:
				fieldSql = fieldSql + ","
			else :
				fieldSql = fieldSql + " "
		return fieldSql

	def executeQuery(self,sql):
		print sql
		cursor = self.getConn()
		cursor.execute(sql)
		values = cursor.fetchall()
		self.close(cursor)
		return values

	def execute(self,sql,params):
		flag = True
		print sql
		def covtUtf8(param):
			if isinstance(param, str):
				return param.decode('gbk').encode('utf-8')
			else:
				return param
		params = filter(covtUtf8, params)
		print params
		cursor = None
		try:
			cursor = self.getConn()
			cursor.execute(sql,params)
		except Exception, e:
			flag = False
			raise e
		finally:
			self.close(cursor)
		return flag

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

	def insert(self,tableName,params):
		return self.insertWithFields(tableName, None, params)

	def insertWithFields(self,tableName,fields,params):
		fieldsSql = ""
		if None != fields and len(fields) > 0:
			fieldsSql = "(%s)"%(self.generateFieldsSql(fields))

		valuesSql = ""
		for x in range(len(params)):
			valuesSql += "?"
			if x < len(params)-1:
				valuesSql += ","

		sql = "insert into %s%s values(%s)"%(tableName,fieldsSql,valuesSql)
		return self.execute(sql, params)




if __name__  == '__main__':
	cf = DbHelper("test.db")
	# values = cf.queryAll('TEST_TABLE')
	# values = cf.query(['id'],'TEST_TABLE')
	# for id in values:
		# print id 
	# cf.execute("insert into TEST_TABLE(id,NAME) values(?,?)", (2,'陈锐2'))
	# cf.insert("TEST_TABLE", (2,'陈锐2'))
	# cf.insertWithFields("TEST_TABLE",['id','NAME'], (2,'陈锐2'))

