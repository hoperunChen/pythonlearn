#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# bad person -->test4.py

class BadPerson(object):
	"""docstring for BadPerson"""
	def __init__(self):
		super(BadPerson, self).__init__()
		self._name = 'xuelai.ye'
		self.curr , self.step = 0, 1

	# 等价于tostring 只用于 直接打印 对象
	def __str__(self):
		return '%s is a bad person' %(self._name)
	#__repr__ 用于直接打印 对象
	__repr__ = __str__

	#迭代 ,有迭代的 需要实现next方法
	def __iter__(self):
		return self

	def next(self):
		rtn = self.curr
		self.curr = self.curr + self.step
		if self.curr > 10 :
			raise StopIteration()
		return rtn

	#要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
	def __getitem__(self, n):
		a, b = 0, 1
		for x in range(n):
			a = a + b
		return a

	#如果get一个不存在的属性,会报错AttributeError: ,解决这个问题 除了添加一个属性之外还可以使用__getattr__()
	def __getattr__(self,attr):
		if attr == 'hello':
			return 'hello badPerson xuelai.ye'
		elif attr == 'hi':
			return attr
		else:
			raise AttributeError('\'BadPerson\' object has no attribute \'%s\'' % attr)

	#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。
	def __call__(self):
		print 'fuck you'
