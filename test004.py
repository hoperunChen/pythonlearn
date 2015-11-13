#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# The second day list类型
print u'声明list-->list = [\'a\',\'b\']'
mylist = ['a','b']
print u'可以直接打印整个list-->print list'
print mylist
print u'可以通过下标访问,同样有下标越界异常'
print mylist[0]
print u'当下标为负数,比如"-1"时,会从最后一个元素开始取值'
print mylist[-1]
print u'获取list的容量'
print len(mylist)
print u'在python中list是没有类型限制的,比如下面一个list中有字符串和int'
mylist1 = ['a',1]
print mylist1

print u'追加元素方法:append(xxx)'
mylist.append(u'append element')
print mylist

print u'插入到某个位置用insert(index,element)'
mylist.insert(1, 'insert element')
print mylist

print u'删除最后的元素用pop()出栈'
mylist.pop()
print mylist

print u'删除某个元素用pop(index)'
mylist.pop(1)
print mylist

print u'要把某个元素替换成别的元素，可以直接赋值给对应的索引位置'
mylist[0] = 'replace'
print mylist

print u'list 可以嵌套'
mylist.append(mylist1)
print mylist

print u'嵌套list取值可以用mylist[-1][0]这种方式'
print mylist[-1][0]

print u'嵌套list的len不会包含子list的长度'
print len(mylist)