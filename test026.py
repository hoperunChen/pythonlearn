#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# collections 内建模块


#namedtuple

'''
namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
并可以用属性而不是索引来引用tuple的某个元素。
这样一来，我们用namedtuple可以很方便地定义一种数据类型，
它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
'''
from collections import namedtuple
Point = namedtuple('Point', ['x','y'])
p = Point(1,2)
print p.x
print p.y


#deque

'''
使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
'''
