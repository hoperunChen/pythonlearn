#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# The second home work
# 1:控制台输入输出
# 2.基础类型
# 3.list和tuple
# 4.dict和set
# 5.条件判断和循环


print u'python 中用type(el)来获取元素类型,通过isinstance(el,str)来判断元素是不是某类型'
a = 1
print type(a)
print isinstance(a,int)

print u'****************判断是否回文数****************************'
num = int(raw_input('set a num:'))
Conversely = [];
new  = 0;
temp = num;
while temp>0:
	rem = temp%10
	print rem
	new = new * 10 + rem 
	temp = temp / 10
print 'new = %d&%d'%(new,num)
if new == num:
	print u'%d是回文数'%(num)
else:
	print u'%d不是回文数'

print u'***************联系list和tuple************************'
mylist = ['a']
print u'mylist的长度是%d'%(len(mylist))
mylist.append('b')
print mylist
mylist.pop()
print mylist
mylist1 = ['a','b','c']
mylist.append(mylist1)
print mylist
mylist.append('s')
mylist.append('s')
mylist.append('s')
mylist.append('s')
print mylist
mylist.insert(1,'e')
print mylist
mylist.pop(2)
print mylist
mylist[3] = 'cr'
print mylist

print u'***************联系tuple************************'
mytuple = (1,'2',3,[1,2,3])
print mytuple
for el in mytuple:
	print type(el)
	if isinstance(el,list):
		el[0]='cr'
print mytuple
