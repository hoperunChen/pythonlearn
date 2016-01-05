#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#模块

' a test module '

__author__ = 'cr' #开发者用户
__doc__ = '''文档说明''' #模块的文档注释

#类似_xxx和__xxx这样的函数或变量就是非公开的（private）

__testprivate = 'ssss'

def helloModule():
	print 'helloModule'

def getTestprivate():
	return __testprivate


#当python XXX.py的时候 类的__name__ 会自动被改为__main__,一般这样都是运行测试方法的
if __name__=='__main__':
    helloModule()