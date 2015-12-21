#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# sorted

print sorted([6,5,3,76,4])


def sotred_str(s1,s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1>u2:
		return 1
	elif u1<u2:
		return -1
	else:
		return 0 
print sorted(['iterable','jsisla','Joskks','aoskks'],sotred_str)
