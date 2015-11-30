#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 生成式
def _print(msg=''):
	print _toUtf8(msg)

def _toUtf8(msg):
	return '%s'%(msg.decode('utf-8'))

_print("如果要生成[1x1, 2x2, 3x3, ..., 10x10]这样的一个列表")

list1 = [x * x for x in range(1,11)]

print list1

_print("for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：[x * x for x in range(1, 11) if x % 2 == 0]")

list1 = [x * x for x in range(1,11) if x % 2 == 0]

print list1