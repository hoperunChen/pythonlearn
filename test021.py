#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 模块调用

import test021.helloM as helloM #导入模块时可以使用别名
#在python中可以对导入做try操作,如果导入失败就导入另外一个
try:
    import json # python >= 2.6
except ImportError:
    import simplejson as json # python <= 2.5


helloM.helloModule() #调用模块中的方法
print helloM.__testprivate
print helloM.getTestprivate()