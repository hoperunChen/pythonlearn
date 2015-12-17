#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# filter

#和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def isprime(num):
	if isinstance(num, int) == 0:
		raise TypeError('num must be int type')
	if num == None:
		return False
	for i in range(2,num):
		print i
		if num % i ==0:
			return False
	return True
print isprime(11)
print filter(isprime, range(1,101))