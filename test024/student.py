#!/usr/bin/env python
# -*- coding: utf-8 -*-  
#学生类

class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name

class Teacher(object):
	__slots__ = ('name','age')
	"""docstring for Teacher"""
	def __init__(self, name):
		super(Teacher, self).__init__()
		self.name = name

class PhysicsTeacher(Teacher):
	__slots__ = ('height')
	"""docstring for PhysicsTeacher"""
	def __init__(self, name):
		super(PhysicsTeacher, self).__init__(name)
		self.name = name

class ChemistryTeacher(Teacher):
	"""docstring for ChemistryTeacher"""
	def __init__(self, name):
		super(ChemistryTeacher, self).__init__(name)
		self.name = name

		