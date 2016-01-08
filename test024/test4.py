#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#订制类

from badPerson import BadPerson

bp = BadPerson()
print bp


for x in bp:
	print x 

print bp[13]

print bp.hello
print bp.hi

#print bp.nimei

bp()