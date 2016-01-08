#!/usr/bin/env python
# -*- coding: utf-8 -*-  


#从student模块中导入Student类
from student import Student

s = Student('s1')
print s.name
#给Student动态绑定年龄属性
s.age  = 18
print s.age

#给Student动态绑定方法
def setAge(self,age):
	self.age = age
from types import MethodType
s.setAge = MethodType(setAge,s,Student)
s.setAge(19)
print s.age

#给一个实例动态绑定年龄和方法对别的实例没有影响
s2 = Student('s2')
# print s2.age

#为了给所有实例绑定方法 ,可以给class绑定方法
Student.setAge = MethodType(setAge,None,Student)
s2.setAge(20)
print s2.age
#为了给所有实例绑定属性,可以给class 绑定属性
Student.hello  = 'sssss'
print s2.hello

#如何限制class的属性?,在类的定义里面加上__slots__ 属性,即可,我在Teacher类里面加上了__slots__属性

from student import Teacher
t = Teacher('t1')
#t.hello = 'hello'
#print t.hello

#__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的!!!!!!!!!!!!!
from student import ChemistryTeacher
ct = ChemistryTeacher('t2')
ct.hello = 'hello'
print ct.hello

#如果子类里也有__slots__ 那么他的限制就是子类的__slots__加上基类的__slots__
from student import PhysicsTeacher
pt = PhysicsTeacher('t3')
pt.height = 183
print pt.height
pt.age = 39
print pt.age
pt.hello = 'hello1'
