#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 匿名函数 lambda


# :号面前是入参,冒号后面是运算方式
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])

x  = lambda x : x * x
print x(2)

#匿名函数也可以作为返回值

def sum(i,j):
	return lambda: i + j

s = sum(1, 3)
print s()