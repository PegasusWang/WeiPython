# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)
# Created Time : Wed Feb 18 18:18:10 2015

# File Name: views.py
# Description:

# :copyright: (c) 2015 by Pegasus Wang.
# :license: MIT, see LICENSE for more details.
"""
# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View
from .wechatUtil import checkSignature
from .wechatService import WechatService


class WechatInterfaceView(View):

    def get(self, request):
        echostr = request.GET.get(u'echostr', None)
        if checkSignature(request):
            return HttpResponse(echostr)

    def post(self, request):
        return HttpResponse(WechatService.processRequest(request))
