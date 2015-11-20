#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 函数的参数
def _print(msg=''):
	print _toUtf8(msg)

def _toUtf8(msg):
	return '%s'%(msg.decode('utf-8'))

_print('默认参数:在函数定义的时候可以设置参数的默认值(默认值最好设置不可变类型),设置了默认值的参数在函数调用的时候可以不填值')
def pingfang(num,mi=2):
	if num == None:
		raise RuntimeError('args num is null')
	rtn = num
	for x in xrange(mi-1):
		rtn = rtn * num
	return rtn
print pingfang(2)
print pingfang(2,3)

_print('可变参数,在参数前面添加一个"*"号可以使该参数成为可变参数,可变参数会自动把参数组装成一个tuple,可变参数可以不填')
def concat(*strs):
	rtn = ''
	for s in strs:
		rtn = rtn + s
	return rtn
print concat('s','bin')
def concat1(one,*strs):
	rtn = one
	for s in strs:
		rtn = rtn + s
	return rtn
print concat('a')

_print('关键字参数,关键字参数允许你传入0个或任意个含参数名的参数,这些关键字参数在函数内部自动组装为一个dict')

def person(name,age,**other):
	print 'name:',name,'age:',age,'other:',other
	
other = {'city':'beijing'}
person('he', 19,**other)


