#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 

import person as p 

class Man(p.Person):
	"""docstring for Man"""
	def __init__(self, name):
		super(Man, self).__init__(name)
		self.name = name
		self.sex = 'man'


	def sayHello(self):
		print 'my name is %s'%self.name 