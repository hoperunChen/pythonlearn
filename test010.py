#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 递归函数
def _print(msg=''):
	print _toUtf8(msg)

def _toUtf8(msg):
	return '%s'%(msg.decode('utf-8'))

_print('函数内可以调用其他函数,如果再某函数内调用函数自己,我们就称该函数为递归函数')
_print('如下面的例子,print_split函数会将一个字符串的每个字符打印出来')

def print_split(msg):
	if len(msg) < 1:
		return;
	else:
		print(msg[len(msg)-1:len(msg)])
		return print_split(msg[0:-1])

print_split('abcde')