#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 迭代
def _print(msg=''):
	print _toUtf8(msg)

def _toUtf8(msg):
	return '%s'%(msg.decode('utf-8'))

_print('在python中for循环可以用于所有可迭代对象中比如dict和string')
mydict = {'a':1,'b':2,'c':3}
for s in mydict:
	print s
for s in 'abcde':
	print s
_print('一般对于dict的迭代都是迭代key,如果要迭代value可以用"for value in dict.itervalues()",如果要同时迭代key和value,可以用"for key, value in d.iteritems()"')
for v in mydict.itervalues():
	print v
for k, v in mydict.iteritems():
	print k, v
_print('如何判断一个元素是不是可便利对象,方法是通过collections模块的Iterable类型判断')
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance((1,2,3),Iterable)
print isinstance(123,Iterable)

_print('如何实现下标迭代,想java那样,python内置的enumerate函数可以把一个list变成索引-元素对,这样就可以同时迭代索引和元素了')
for i,el in enumerate([1,2,3]):
	print i,el