#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#机器人

import db.dbhelper as db
import uuid
dbh = db.DbHelper('db/test.db')


def getAnwser(question):
	print u'我不知道应该回答什么,请告诉我我应该回答什么呢?'
	anwser = raw_input()
	if None == anwser or len(anwser) < 1:
		print u'小气鬼不告诉我算了'
	else:
		dbh.insert('question_anwser',(str(uuid.uuid1()),question,anwser))
		print u'谢谢你,么么哒!'

while True:
	question = raw_input()
	if None == question or len(question) < 1 :
		continue
	question = question.replace(' ', '') 
	# print question
	values = dbh.executeQuery('select anwser from question_anwser where question = ?',(question,))
	if None == values or len(values) < 1 :
		getAnwser(question)
	else:
		print values[0][0]


