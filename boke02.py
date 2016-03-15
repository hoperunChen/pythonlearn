#!/usr/bin/env python
# -*- coding: utf-8 -*-  

USER_NAME = 'a'
USER_PASS = '123'
userName = raw_input('Please enter your name:')
if userName == USER_NAME:
	passWord = raw_input('Please enter your password:')
	if passWord == USER_PASS:
		print 'logged in.'
	else:
		print 'Your password is wrong.'

else:
	print 'Your user name is wrong.'


