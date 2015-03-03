# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)
# Created Time : Wed Feb 18 18:29:06 2015

# File Name: wechatEvent.py
# Description:

# :copyright: (c) 2015 by Pegasus Wang.
# :license: MIT, see LICENSE for more details.
"""


class BaseEvent(object):
    """base event class"""
    def __init__(self):
        self.ToUserName = u''
        self.FromUserName = u''
        self.CreateTime = 0L
        self.MsgType = u''
        self.Event = u''

    def getToUserName(self):
        return self.ToUserName

    def setToUserName(self, toUserName):
        self.ToUserName = toUserName

    def getFromUserName(self):
        return self.FromUserName

    def setFromUserName(self, fromUserName):
        self.FromUserName = fromUserName

    def getCreateTime(self):
        return self.CreateTime

    def setCreateTime(self, createTime):
        self.CreateTime = createTime

    def getMsgType(self):
        return self.MsgType

    def setMsgType(self, msgType):
        self.MsgType = msgType

    def getEvent(self):
        return self.Event

    def setMsgId(self, event):
        self.Event = event


class SubscribeEvent(BaseEvent):
    """subscribe event class"""
    def __init__(self):
        super(SubscribeEvent, self).__init__()


class QRCodeEvent(BaseEvent):
    """scan QR code event class"""
    def __init__(self):
        super(QRCodeEvent, self).__init__()
        self.EventKey = u''
        self.Ticket = u''

    def getEventKey(self):
        return self.EventKey

    def setEventKey(self, eventKey):
        self.EventKey = eventKey

    def getTicket(self):
        return self.Ticket

    def setTicket(self, ticket):
        self.Ticket = ticket


class LocationEvent(BaseEvent):
    """upload location event class"""
    def __init__(self):
        super(LocationEvent, self).__init__()
        self.Latitude = u''
        self.Longitude = u''
        self.Precision = u''

    def getLatitude(self):
        return self.Latitude

    def setLatitude(self, latitude):
        self.Latitude = latitude

    def getLongitude(self):
        return self.Longitude

    def setLongitude(self, longtitude):
        self.Longitude = longtitude

    def getPrecision(self):
        return self.Precision

    def setPrecision(self, precision):
        self.Precision = precision


class MenuEvent(BaseEvent):
    """customize menu class"""
    def __init__(self):
        super(MenuEvent, self).__init__()
        self.EventKey = u''

    def getEventKey(self):
        return self.EventKey

    def setEventKey(self, eventKey):
        self.EventKey = eventKey
