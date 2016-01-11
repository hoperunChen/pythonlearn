#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 异常处理


def aErr():
	raise ValueError('hhhslskdk')

try:
	aErr()
except ValueError, e:
	print 'valueError',e
else:
	print 'no error'
finally:
	print 'finally'
