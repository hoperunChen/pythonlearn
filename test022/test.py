#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#test

' a test module '

__author__ = 'cr' #开发者用户
__doc__ = '''文档说明''' #模块的文档注释

import person as p

person = p.Person()

print person.name # 成员变量是直接可以访问的
person.setName('ssss') #可以使用set修改成员变量
person.sayHello() #通过方法获取成员变量
 #员变量被修改
print person.name