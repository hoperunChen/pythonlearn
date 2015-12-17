#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 管理nginx的upstream
import sys
import os
#print 'fileName:%s'%sys.argv[0] #文件名
#第一个参数 要进行的操作 must 
#-a  添加 需要带参数: [2]>>>:upstream名称  [3]>>>:添加的地址
#-d  删除 需要带参数: [2]>>>:upstream名称  [3]>>>:删除的地址
#-l  查询列表 可以带参数: [2]>>>:upstream名称

#CONF_FILE_PATH = 'E:\Work\ChinaUnicom\\nginx\upstream.conf'
#CONF_NGINX_PATH = 'E:\Work\ChinaUnicom\\nginx\upstream.conf'
CONF_FILE_PATH = '/usr/local/nginx/conf/upstream.conf'
CONF_NGINX_PATH = '/usr/local/nginx/sbin/nginx'

def _print(msg=''):
	print _toUtf8(msg)

def _toUtf8(msg):
	return '%s'%(msg.decode('utf-8'))

def printHelp():
	_print('-l    Query all backend server list\n\tupstreamName:Query name for the [upstreamName] backend server list')
	_print('-a    Add back-end server\n\tupstreamName:Add back-end server to [upstreamName]\n\tpath:Backend server address is [path]')
	_print('-d    Delete backend server\n\tupstreamName:Delete backend server from [upstreamName]\n\tpath:Backend server address is [path]')
	_print('\n*Path must be "ip: port" format')

def listUpstream(context,upstreamName = None):
	if context == None or len(context) < 1:
		return ''
	flag = True
	upstreamDict = {}
	_context = context
	while flag:
		name = _context[_context.find('upstream ')+len('upstream '):_context.find('{')].strip()
		value = _context[_context.find('{')+1:_context.find('}')]
		def getValueList(value):
			rtn = []
			if value == None or len(value.strip()) < 1:
				return rtn
			_flag = True
			while _flag:
				rtn.append(value[:value.find(';')].strip())
				value = value[value.find(';')+1:].strip()
				if len(value) <1:
					_flag = False
			return rtn
		upstreamDict[name] = getValueList(value)
		_context = _context[_context.find('}')+1:].strip()
		if len(_context) < 1 :
			flag = False

	if upstreamName == None:
		return upstreamDict
	else:
		if upstreamName in upstreamDict:
			return upstreamDict[upstreamName]
		else:
			_print('No upstream')

def addUpstream(context,upstreamName,path):
	if upstreamName == None or len(upstreamName) < 1:
		raise RuntimeError('upstreamName can not be None')
	if path == None or len(path) < 1:
		raise RuntimeError('path can not be None')
	updict = listUpstream(context)
	upList = updict[upstreamName]
	#地址是否已经存在,如果存在就不再添加,不存在添加
	if pathContains(upList,path) != -1:
		#存在
		_print('upstream:'+upstreamName+' Address already exists:'+path)
		return
	else:
		#不存在
		upList.append('server '+path)
		updict[upstreamName] = upList
	#print updict[upstreamName]
	#保存 到文件
	saveToFile(updict)

def delUpstream(context,upstreamName,path):
	if upstreamName == None or len(upstreamName) < 1:
		raise RuntimeError('upstreamName can not be None')
	if path == None or len(path) < 1:
		raise RuntimeError('path can not be None')
	updict = listUpstream(context)
	upList = updict[upstreamName]
	#地址是否已经存在,如果存在就删除,不存在跳过
	if pathContains(upList,path) != -1:
		#存在删除
		while True:
			upList.pop(pathContains(upList,path))
			if pathContains(upList,path) == -1:
				break
		updict[upstreamName] = upList
	else:
		#不存在
		_print('upstream:'+upstreamName+' No address:'+path)
		return
	#print updict[upstreamName]
	#保存 到文件
	saveToFile(updict)

def saveToFile(updict):
	inputStr = '';
	if None == updict or len(updict) <1 :
		return 
	for key in updict:
		inputStr += 'upstream '+key+' {\n'
		upList = updict[key]
		for ipList in upList:
			inputStr += '\t'+ipList+';\n'
		inputStr += '\n}\n'
	print inputStr
	with open(CONF_FILE_PATH, 'w') as f:
	    f.write(inputStr)
	reloadNginx()

def pathContains(upList,path):
		rtn = -1
		for pathStr in upList:
			if pathStr.find(path) != -1:
				#存在
				rtn =  upList.index(pathStr)
		return rtn

def reloadNginx():
	os.system(CONF_NGINX_PATH+' -s reload')

#os.system("cls") #windows
os.system("clear") #linux
if len(sys.argv) <2 or sys.argv[1] == None:
	_print('Please enter a parameter query, if it is not clear, please call -help')
	exit(0)
doWhat = sys.argv[1] 
upstreamName = len(sys.argv)>2 and sys.argv[2] or None
path = len(sys.argv)>3 and sys.argv[3] or None
print CONF_FILE_PATH
with open(CONF_FILE_PATH, 'r') as f:
	context = f.read()
#print u'读取到的配置文件:\n%s'%context

if doWhat == "-l":
	print listUpstream(context,upstreamName)
elif doWhat == "-a":
	addUpstream(context,upstreamName,path)
elif doWhat == "-d":
	delUpstream(context,upstreamName,path)
elif doWhat == "-help":
	printHelp()



