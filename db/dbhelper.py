#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#dbHelper
import sqlite3

class DbHelper(object):
	def __init__(self, path):
		super(DbHelper, self).__init__()
		self.path = path
		self.conn = None

	def covtUtf8(self,data):
		if isinstance(data, str):
			return data.decode('gbk').encode('utf-8')
		else:
			return data

	def covtGBK(self,data):
		newData = []
		for d in data:
			_temp = d
			if isinstance(d, str):
				_temp = d.decode('utf-8').encode('gbk')
			newData.append(_temp)
		return newData

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

	def executeQueryParams(self,sql,params):
		#print sql
		#params = filter(self.covtUtf8, params)
		#print params
		cursor = self.getConn()
		cursor.execute(sql,params)
		values = cursor.fetchall()
		self.close(cursor)

		new_values = []
		for data in values:
			data = self.covtGBK(data)
			new_values.append(data)
		return new_values

	def executeQuery(self,sql,params = None):
		#print sql
		cursor = self.getConn()
		if None == params:
			cursor.execute(sql)
		else:
			cursor.execute(sql,params)
		values = cursor.fetchall()
		self.close(cursor)

		new_values = []
		for data in values:
			#data = self.covtGBK(data)
			new_values.append(data)
		return new_values

	def execute(self,sql,params):
		flag = True
		#print sql
		#params = filter(self.covtUtf8, params)
		#print params
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

	'''
		插入数据
		params:
			tableName:表名
			params:参数列表 (1,'陈锐3')
	'''
	def insert(self,tableName,params):
		return self.insertWithFields(tableName, None, params)


	'''
		插入数据
		params:
			tableName:表名
			fields:名称列表 ['id','name']
			params:参数列表 (1,'陈锐3')
	'''
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
	# values = cf.executeQueryParams("select * from TEST_TABLE where NAME = ?", ('陈锐',))
	# print values
	values = cf.queryAll('TEST_TABLE')
	# values = cf.query(['id'],'TEST_TABLE')
	#for id,name in values:
		#print id + '-->' +name
	# cf.execute("insert into TEST_TABLE(id,NAME) values(?,?)", (2,'陈锐2'))
	# cf.insert("TEST_TABLE", (2,'陈锐2'))
	# cf.insertWithFields("TEST_TABLE",['id','NAME'], (2,'陈锐2'))

