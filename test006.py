#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# The second day 条件语句和循环语句
print u'''条件语句语法:
if [条件1]:
	<执行1>
	<执行2>
elif [条件2]:
	<执行3>
	<执行4>
else
	<执行5>
'''

print u'''循环语句-->for:
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum
mylist = ['a','b']
for x in mylist:
    print x
'''
print u'range(5)生成的序列是从0开始小于5的整数'

print u'''循环语句-->while:
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print sum
mylist['a','b']
for x in mylist:
    print x
'''
print u'''循环语句-->while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
'''

print u'条件和循环练习:用户输入一个大于0的数字,计算从0加到这个数字的和,输入小于等于0的数字退出'
while True:
	userNum = int(raw_input('set a Num:'))
	if userNum <= 0 :
		exit()
		print u'退出'
	numList = range(userNum+1)
	sumNum = 0;
	for n in numList:
		sumNum += n
	print sumNum
