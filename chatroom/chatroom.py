#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# server tcp编程

import socket
import time, threading

# IP地址和端口应该放在配置文件里
ipaddr = '127.0.0.1' 
port = 5432

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ipaddr,port))
server.listen(5)
print 'chat room server bind for 127.0.0.1'

def tcplink(clientSock, clientAddr):
	print 'Accept new connection from %s:%s...' %(clientAddr)
	clientSock.send('Welcome!')
	while True:
		data = clientSock.recv(1024) #每次接受1k的数据
		time.sleep(1)
		if data == 'exit' or not data:
			break
		print 'receive message from %s:%s;-->%s' %(clientAddr[0],clientAddr[1],data)
		clientSock.send('hello %s' % data)
	clientSock.close()
	print 'Connection from %s:%s closed.' % clientAddr

while True:
	print 'chat room Service has been started'
	clientSock, clientAddr = server.accept()
	t = threading.Thread(target=tcplink, args=(clientSock, clientAddr))
	t.start()
