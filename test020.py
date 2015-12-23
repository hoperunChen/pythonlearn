#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 装饰器

#所谓的装饰器函数,就是定义一个参数是函数类型的函数,接受被装饰的函数,然后返回一个函数,这个返回函数包含被装饰函数以及装饰内容如下:
def printSth(fun):
	def wrapper():
		print 'befor call %s()'%fun.__name__
		rtn = fun()
		print 'after call:%s()'%fun.__name__
		return rtn
	return wrapper
#想要将装饰器引用到被装饰函数,需要在被装饰函数的定义上方使用@注解该方法
@printSth
def sss():
	print 'aaaaaaaaaaaaa'
	return 'call'
#调用的sss函数实际上是sss函数的一个装饰函数,实际上等于 printSth(sss)()
print sss()
#在这个时候sss函数的name实际上是 wrapper
print sss

#如果想要sss的name是自己的name 需要:

import functools
def printSthOther(func):
    @functools.wraps(func)
    def wrapper():
		print 'befor call %s()'%func.__name__
		rtn = func()
		print 'after call:%s()'%func.__name__
		return rtn
    return wrapper

@printSthOther
def sssOther():
	print 'aaaaaaaaaaaaa'
	return 'call'
print sssOther()
print sssOther

#注解还可以传递参数:
def argsWrapper(wraArgs):
	def decorator(func):
	    @functools.wraps(func)
	    def wrapper(*args,**kw):
			print 'befor call %s()'%func.__name__
			rtn = func(*args,**kw)+wraArgs
			print 'after call:%s()'%func.__name__
			return rtn
	    return wrapper
	return decorator

@argsWrapper('sssOther')
def sssArgs(msg):
	print 'aaaaaaaaaaaaa:%s'%msg
	return 'call'
#这样嵌套的调用就等于   argsWrapper('hello args')(sssArgs)('ssisoslsi')
print sssArgs('ssisoslsi')
print sssArgs


#课后练习:
#再思考一下能否写出一个@log的decorator，使它既支持：
#@log
#def f():
#    pass
#又支持：
#
#@log('execute')
#def f():
#    pass
def _log(text=''):
	if 0 == hasattr(text,'__call__'):
		def dec(func):
			@functools.wraps(func)
			def wra(*args,**kw):
				print '-----befor'
				rtn = func(*args,**kw)
				print '-----after'
				print text
			return wra
		return dec
	else:
		@functools.wraps(text)
		def wra(*args,**kw):
			print '-----befor'
			rtn = text(*args,**kw)
			print '-----after'
			return rtn
		return wra
@_log
def f():
	print 'fffffffffffff'
@_log('#####')
def ff():
	print 'fffffffffffff'
print '****************************homework****************************'
print 'have not Args:'
f()
print 'have Args:'
ff()


print '****************************ext****************************'
#装饰器接受的参数可以是函数
def log(befor='',after=''):
	if 0 == hasattr(befor,'__call__'):
		def befor():
			pass
	elif 0 == hasattr(after,'__call__'):
		def after():
			pass
	def dec(func):
		@functools.wraps(func)
		def wra(*args,**kw):
			befor()
			rtn = func(*args,**kw)
			after()
			return rtn
		return wra
	return dec

def befor():
	print 'befor call'
def after():
	print 'after call'
@log(befor)
def sayHello(name,ages,isboy):
	print 'hello everyOne my name is %s,I am %d years old this year,I am a %s'%(name,ages,'boy' if isboy else 'gril')
sayHello('cherry',18,True)
	