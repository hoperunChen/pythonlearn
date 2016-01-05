#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# class Person

class Person(object):
	"""docstring for Person"""
	def __init__(self):
		super(Person, self).__init__()
		self._age = 111

	name = 'aaaa'
	def setName(self,name):
		self.name = name

	def sayHello(self):
		print self.name