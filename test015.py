#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# map/reduce
def _print(msg=''):
	print _toUtf8(msg)

def _toUtf8(msg):
	return '%s'%(msg.decode('utf-8'))

#lambda表達式:可以接受多个参数,并且返回一个值,.如下 接受了x,y两个参数,返回x*10+y的值;lambda中不能有多个表达式
print (lambda x,y: x*10+y)(1,2)

def testMap(x):
	return x+10
myList = [1,2,3]
print map(testMap, myList)
#[11, 12, 13]
print map(lambda x : x*2, [1,2,3,[2,3]])
#[2, 4, 6, [2, 3, 2, 3]]
def testMap1(a,b):
	return a*10+b
myList1 = [4,5,6]
print map(testMap1, myList,myList1)
#[14, 25, 36]

_print('python的map(fun,list)方法就是把list的每一个值分别作为参数调用fun方法,最后将return作为list返回')


#reduce
def myreduce(x,y):
	return x*100+y*10
#myreduce 方法必须双参,不能多也不能少
print reduce(myreduce, [1,2,3])
#12030

_print('reduce(fn,[x,y,z])方法就是fn(fn(x,y),z)')



#map和reduce组合例子:
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
rtn = str2int('352567')
print '%d---%s'%(rtn,type(rtn))


#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。
#str.capitalize() 方法,将字符串的首字母大写,其他字符小写

print map(lambda name:name.capitalize(), ['IsskslI','jjjKlK','skslLLL'])

#请编写一个prod()函数，可以接受一个list并利用reduce()求积

print reduce(lambda x,y:x*y, [1,2,3])

