#!/usr/bin/env python
# -*- coding: utf-8 -*-  
import urllib
import urllib2  
 
url = 'http://172.20.2.130:8080/portal/jsp/login.jsp?returnURL=vm&consoleOf=maintain'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0'
referer = 'http://172.20.2.130:8080/portal/jsp/login.jsp?returnURL=vm&consoleOf=maintain'
values = {'username' : 'clouddata_jh',  'password' : 'password','portalType':'private','securityLevel':'1'}
headers = { 'User-Agent' : user_agent , 'Referer' : referer}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()
print page