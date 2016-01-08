#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 

import man
import woman as wo
import person

manEl = man.Man('cherry')
womanEl = wo.Woman('boke')

manEl.sayHello()

womanEl.sayHello()

def sayHello(person):
	person.sayHello()
	print 'I\'m a %s'%person.sex

sayHello(manEl)
sayHello(womanEl)
#显示类的属性
print dir(womanEl)
#获取类的类型
print type(manEl)
#判断类的类型
print isinstance(manEl, person.Person)