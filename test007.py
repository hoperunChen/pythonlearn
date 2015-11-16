#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# The second day dict and set
print u'dict等价于java中的map,声明方式: mydict = {"key":"value"}'
mydict = {'a':1,'b':'xiaoming','c':False}
print mydict
print u'取出dict中key为b的值'
print mydict['b']
print u'可以用"\'b\' in mydict"来判断在mydict中是否存在b这个key'
print 'b' in mydict
print u'还可以通过get方法去获取元素,如果元素不存在,那么就会返回None或者自己制定的值'
print mydict.get('d')
print mydict.get('d',u'指定返回:xiaofang')
print u'dict用pop(key)来删除一个元素'
mydict.pop('b')
print mydict


print u'在python中set用来存储一组不重复的集合声明语法: s = set([1,2,3])'
s = set([1,2,3])
print s
for es in s:
	print es
print u'使用add来向set中添加元素'
s.add(1)
s.add(4)
print s


t = (1,2,3)
s.add(t)
print s

mydict[t] = 'hello'
print mydict
