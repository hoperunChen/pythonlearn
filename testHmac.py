#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# 生成式
import base64
import hmac
import urllib
from hashlib import sha1

secret_access_key = 'testASK'

# 前面生成的被签名串
string_to_sign = "unifacc%2FaccessKey%3DtestAK%26action%3DdescribeInstances%26count%3D1%26period%3D1"
h = hmac.new(secret_access_key, digestmod=sha1)
h.update(string_to_sign)
sign = base64.b64encode(h.digest()).strip()
print sign
signature = urllib.quote_plus(sign)
print signature