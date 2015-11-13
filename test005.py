#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# The second day tuple类型

print u'另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改'
print u'声明方式:mytuple = (e1,e2)'
mytuple = ('e1','e2')
print mytuple
print u'声明只有一个元素的tuple时,要在第一个元素后面添加逗号,打印时也会显示逗号'
mytuple1 = ('e1',)
print mytuple1

print u'tuple可以嵌套list,tuple中的list可以修改,但是tuple的元素不可以修改'
mylist = ['a','b']
print mylist;
mytuple2 = ('e1',mylist)
print mytuple2
mytuple2[1].append('append')
print mytuple2