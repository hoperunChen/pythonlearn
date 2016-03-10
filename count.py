#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

#定义ip访问流量和ip访问次数字典
ipflow = {}
ipnum = {}

#定义匹配正则
ipre = re.compile(r'(\d{1,3}\.){1,3}\d{1,3}')
flowre = re.compile('"'+'\D'+str(200)+'\D(\d+)\D')
#定义http状态码(你可以把日志里经常出现的状态码放在前面)
code = [302,206,100,101,102,201,202,203,204,205,207,300,301,303,304,305,306,307,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,421,422,424,425,426,449,500,501,502,503,504,505,506,507,509,510]

#读取日志
f = open("E:/Work/access.log","r")
logs = f.readlines()
f.close()
#统计ip访问次数和流量
for line in logs:
    if not line.strip():continue
    f = line.split('\t')
    ip = ipre.search(f[0])
    flow = flowre.findall(f[0])
    if not flow:
        for i in code:
            codere = re.compile('"'+'\D'+str(i)+'\D(\d+)\D')
            flow = codere.findall(f[0])
            if flow:
                break
            elif i == 510:
                if not flow:
                    flow = ['0']
    try:
        if ip.group() in set(k.lower() for k in ipflow):
            ipnum[ip.group()] += 1
            ipflow[ip.group()] = int(ipflow[ip.group()]) + int(flow[0])
        else:
            ipnum[ip.group()] = 1
            ipflow[ip.group()] = int(flow[0])
    except ValueErro:
        continue

#显示单个ip访问的次数和流量
for k in ipnum:
    print "访问IP：%s 访问次数：%d 访问流量：%.3fM" % (k,int(ipnum[k]),float(ipflow[k])/float(1000))