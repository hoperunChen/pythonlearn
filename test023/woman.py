#!/usr/bin/env python
# -*- coding: utf-8 -*-  

import person as p 

class Woman(p.Person):
	"""docstring for Woman"""
	def __init__(self, name):
		super(Woman, self).__init__(name)
		self.name = name
		self.sex = 'woman'