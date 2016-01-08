#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 多重继承

class RunableMixin(object):
	"""docstring for RunableMixin"""
	def __init__(self):
		super(RunableMixin, self).__init__()

	def run(self):
		print 'running'
