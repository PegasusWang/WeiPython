# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)
# Created Time : Fri Feb 20 22:31:30 2015

# File Name: urls.py
# Description:

# :copyright: (c) 2015 by Pegasus Wang.
# :license: MIT, see LICENSE for more details.
"""
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from wechat import views


urlpatterns = patterns('',
    url(r'^$', csrf_exempt(views.WechatInterfaceView.as_view())),
)