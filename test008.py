#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 函数的定义,空函数,多个返回值
print u'定义一个函数要使用"def functionName(args):"定义函数,在缩进中写实现,return 返回'
def my_abs(number):
	if number >= 0:
		rtn =  number
	else:
		rtn = -number
	print rtn
	return rtn;
my_abs(-3)
my_abs(4)

print u'如果你想定义一个函数什么也不做可以用pass语句,pass还可以用在其他地方,比如if/for'
def testPass():
	print 'pass'
	pass
testPass()

print u'可以对参数进行检查,并且抛出异常'
def my_abs(number):
	if not isinstance(number,(int,float)):
		raise TypeError('the my_abs function need a args which type is int or float,but actual args type is %s'%(type(number)))
	if number >= 0:
		rtn =  number
	else:
		rtn = -number
	print rtn
	return rtn;
#my_abs(None)
#my_abs('sss')
my_abs(-19)

print u'函数可以同时返回多个值，但其实就是一个tuple。'
def returnMultiple():
	return 1,2,'abc'
a,b,c = returnMultiple()
print 'a=%d'%a
print 'b=%d'%b
print 'c=%s'%c
print u'实际返回的是:%s' %(returnMultiple(),)
