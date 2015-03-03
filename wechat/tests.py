# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)
# Created Time : Tue Mar  3 19:44:02 2015

# File Name: tests.py
# Description:

"""
import requests
import codecs

f = codecs.open(u'post.xml', u'r', u'utf-8')
content = u''.join(f.readlines())
f.close()

res = requests.post(u'http://2.pegasuswang.sinaapp.com/wechat/', data=content.encode(u'utf-8'))
print res.text
