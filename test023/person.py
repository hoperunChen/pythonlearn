#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 

class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name = name

	def sayHello(self):
		print 'my name is',self.name

	