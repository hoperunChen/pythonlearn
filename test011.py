#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 切片
def _print(msg=''):
	print _toUtf8(msg)

def _toUtf8(msg):
	return '%s'%(msg.decode('utf-8'))

print('在编程中取list/tuple或字符串的某一部分(substring)是很常见的操作,在python中只需要list[0:1]就可以了,我们称他为切片')

l = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取L的第2,3个元素
l1 = l[1:3]
print l1
#如果是从第一个元素开始取,也就是第一个数字是0的情况下可以省略0
l2 = l[0:3]
print l2
#同时支持倒数切片
l3 = l[-3:-2]
print l3
#注意打印最后一个元素不是[-1:0]而是[-1:]
l4 = l[-1:]
print l4
#字符串和tuple都算一种list,都可以用切片操作