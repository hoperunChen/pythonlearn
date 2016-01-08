#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 属性注解,多重继承
class Boy(object):
	"""docstring for Boy"""
	def __init__(self):
		super(Boy, self).__init__()
		self._age = 18
	#一般都要写getter和setter,在python中只需要写注解就可以
	@property
	def name(self):
		print 'Boy.getName'
		return self._name
	
	@name.setter
	def name(self,value):
		print 'Boy.setName'
		if value == 'cherry':
			raise ValueError('cherry can\'t be name')
		self._name = value

	#可以只设置getter,就是只读
	@property
	def age(self):
	    return self._age
