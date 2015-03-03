# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)
# Created Time : Wed Feb 18 18:18:10 2015

# File Name: wechatMessage.py
# Description:

# :copyright: (c) 2015 by Pegasus Wang.
# :license: MIT, see LICENSE for more details.
"""


class BaseMessage(object):
    """base message class"""
    def __init__(self):
        self.ToUserName = u''
        self.FromUserName = u''
        self.CreateTime = 0L
        self.MsgType = u''
        self.MsgId = 0L

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

    def getMsgId(self):
        return self.MsgId

    def setMsgId(self, msgId):
        self.MsgId = msgId


class TextMessage(BaseMessage):
    """text message class"""
    def __init__(self):
        super(TextMessage, self).__init__()
        self.Content = u''

    def getContent(self):
        return self.Content

    def setContent(self, content):
        self.Content = content


class ImageMessage(BaseMessage):
    """image message class"""
    def __init__(self):
        super(ImageMessage, self).__init__()
        self.PicUrl = u''

    def getPicUrl(self):
        return self.PicUrl

    def setPicUrl(self, picUrl):
        self.PicUrl = picUrl


class VoiceMessage(BaseMessage):
    """voice message class"""
    def __init__(self):
        super(VoiceMessage, self).__init__()
        self.MediaId = u''
        self.Format = u''
        self.Recognition = u''

    def getMediaId(self):
        return self.MediaId

    def setMediaId(self, mediaId):
        self.MediaId = mediaId

    def getFormat(self):
        return self.Format

    def setFormat(self, format):
        self.Format = format

    def getRecognition(self):
        return self.Recognition

    def setRecognition(self, recognition):
        self.Recognition = recognition


class VideoMessage(BaseMessage):
    """video message class"""
    def __init__(self):
        super(VideoMessage, self).__init__()
        self.MediaId = u''
        self.ThumbMediaId = u''

    def getMediaId(self):
        return self.MediaId

    def setMediaId(self, mediaId):
        self.MediaId = mediaId

    def getThumbMediaId(self):
        return self.ThumbMediaId

    def setThumbMediaId(self, thumbMediaId):
        self.ThumbMediaId = thumbMediaId


class LocationMessage(BaseMessage):
    """location message class"""
    def __init__(self):
        super(LocationMessage, self).__init__()
        self.Location_X = u''
        self.Location_Y = u''
        self.Scale = u''
        self.Label = u''

    def getLocation_X(self):
        return self.Location_X

    def setLocation_X(self, location_X):
        self.Location_X = location_X

    def getLocation_Y(self):
        return self.Location_Y

    def setLocation_Y(self, location_Y):
        self.Location_Y = location_Y

    def getScale(self):
        return self.Scale

    def setScale(self, scale):
        self.Scale = scale

    def getLabel(self):
        return self.Label

    def setLabel(self, label):
        self.Label = label


class LinkMessage(BaseMessage):
    """link message class"""
    def __init__(self):
        super(LinkMessage, self).__init__()
        self.Title = u''
        self.Description = u''
        self.Url = u''

    def getTitle(self):
        return self.Title

    def setTitle(self, title):
        self.Title = title

    def getDescription(self):
        return self.Description

    def setDescription(self, description):
        self.Description = description

    def getUrl(self):
        return self.Url

    def setUrl(self, url):
        self.Url = url
