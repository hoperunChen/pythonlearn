#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# class Person

class Person(object):
	"""docstring for Person"""

	#类的初始化
	def __init__(self):
		super(Person, self).__init__()
		self.__age = 111
		self.__name = 'aaaa'
	#类的方法的第一个参数都是self,并且调用的时候不需要传递
	def setName(self,name):
		self.__name = name

	def getName(self):
		print self.__name