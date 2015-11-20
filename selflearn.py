#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 练习

FGF = '************************'
LINE = '\n'
TAB = '\t'
YES = 'Y'
No = 'N'

def _print(msg=''):
	print _toUtf8(msg)

def _toUtf8(msg):
	return '%s'%(msg.decode('utf-8'))

def main(args=None):
	if(args!=None):
		if not isinstance(args, dict):
			raise TypeError("shoud set a dict args")
	else:
		uIn = helloPage()
		if uIn == '1':
			login()
		elif uIn == '2':
			response = register()
			if response['code']==-1:
				main()
			else:
				doLogin(response)



def helloPage():
	_print(FGF+'欢迎使用'+FGF)
	_print('请选择:')
	_print(TAB+'1.登录')
	_print(TAB+'2.注册')
	_print(TAB+'3.退出')
	_print('请输入序号(回车提交):')
	return raw_input()

def login():
	#TODO 
	_print('开始登录')
	pass

def doLogin(request):
	#TODO 
	_print('doLogin:'+request['userName']+','+request['userPass'])
	pass

def register():
	rtn = {'userName':None,'userPass':None,'code':-1}
	_print(FGF+'注册'+FGF)
	_print('请输入用户名:')
	userName  = raw_input()
	_print('请输入密码:')
	userPass = raw_input()
	_print('以下是您的输入信息请确认:')
	_print('用户名:'+userName)
	_print('密码:'+userPass)
	while True:
		_print('是否确认或退出(Y/N/exit)')
		uIn = raw_input()
		if uIn.upper().strip() == YES:
			rtn = doRegister(userName, userPass)
			break
		elif uIn.upper().strip() == No:
			rtn = register()
			break
		elif uIn.upper().strip() == 'EXIT':
			rtn['code'] = -1
			break
	return rtn

def doRegister(userName,userPass):

	#TODO 注册功能
	rtn = {'userName':None,'userPass':None,'code':-1}
	rtn['code'] = 1
	rtn['userName'] = userName
	rtn['userPass'] = userPass
	return rtn;

main()





