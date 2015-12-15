#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 高阶函数
def _print(msg=''):
	print _toUtf8(msg)

def _toUtf8(msg):
	return '%s'%(msg.decode('utf-8'))

_print('在python中变量可以是函数,函数名是变量,函数可以作为参数传递')

abs_n = abs
print abs_n(-11)

def jisuan(x,y,fun):
	if x == None:
		print 'x can not be null'
		return
	if y == None:
		print 'y can not be null'
		return
	if fun == None:
		print 'fun can not be null'
		return 
	if 0 == hasattr(fun,'__call__') :
		raise TypeError('fun shoud to be a  function')
	return fun(x)+fun(y)
	
print(jisuan(1, 1, abs))