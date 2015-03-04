# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)
# Created Time : Wed Feb 18 18:58:39 2015

# File Name: wechatReply.py
# Description:

# :copyright: (c) 2015 by Pegasus Wang.
# :license: MIT, see LICENSE for more details.
"""


class BaseReply(object):
    """base reply message class"""
    def __init__(self):
        self.ToUserName = u''
        self.FromUserName = u''
        self.CreateTime = 0L
        self.MsgType = u''

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


class TextReply(BaseReply):
    """text reply message class"""
    def __init__(self):
        super(TextReply, self).__init__()
        self.Content = u''

    def getContent(self):
        return self.Content

    def setContent(self, content):
        self.Content = content


class Image(object):
    """image class"""
    def __init__(self):
        self.MediaId = u''

    def getMediaId(self):
        return self.MediaId

    def setMediaId(self, mediaId):
        self.MediaId = mediaId


class ImageReply(BaseReply):
    """image reply message class"""
    def __init__(self):
        super(ImageReply, self).__init__()
        self.Image = Image()

    def getImage(self):
        return self.Image

    def setImage(self, image):
        self.Image = image


class Voice(object):
    """voice class"""
    def __init__(self):
        self.MediaId = u''

    def getMediaId(self):
        return self.MediaId

    def setMediaId(self, mediaId):
        self.MediaId = mediaId


class VoiceReply(BaseReply):
    """voice reply message class"""
    def __init__(self):
        super(VoiceReply, self).__init__()
        self.Voice = Voice()

    def getVoice(self):
        return self.Voice

    def setVoice(self, voice):
        self.Voice = voice


class Video(object):
    """video class"""
    def __init__(self):
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


class VideoReply(BaseReply):
    """video reply message class"""
    def __init__(self):
        super(VideoReply, self).__init__()
        self.Video = Video()

    def getVideo(self):
        return self.Video

    def setVideo(self, video):
        self.Video = video


class Music(object):
    """music class"""
    def __init__(self):
        self.Title = u''
        self.Description = u''
        self.MusicUrl = u''
        self.HQMusicUrl = u''
        self.ThumbMediaId = u''

    def getTitle(self):
        return self.Title

    def setTitle(self, title):
        self.Title = title

    def getDescription(self):
        return self.Description

    def setDescription(self, description):
        self.Description = description

    def getMusicUrl(self):
        return self.MusicUrl

    def setMusicUrl(self, musicUrl):
        self.MusicUrl = musicUrl

    def getHQMusicUrl(self):
        return self.HQMusicUrl

    def setHQMusicUrl(self, musicUrl):
        self.HQMusicUrl = musicUrl

    def getThumbMediaId(self):
        return self.ThumbMediaId

    def setThumbMediaId(self, thumbMediaId):
        self.ThumbMediaId = thumbMediaId


class MusicReply(BaseReply):
    """music reply message class"""
    def __init__(self):
        super(MusicReply, self).__init__()
        self.Music = Music()

    def getMusic(self):
        return self.Music

    def setMusic(self, music):
        self.Music = music


class Article(object):
    """article class"""
    def __init__(self):
        self.Title = u''
        self.Description = u''
        self.PicUrl = u''
        self.Url = u''

    def getTitle(self):
        return self.Title

    def setTitle(self, title):
        self.Title = title

    def getDescription(self):
        return self.Description

    def setDescription(self, description):
        self.Description = description

    def getPicUrl(self):
        return self.PicUrl

    def setPicUrl(self, picUrl):
        self.PicUrl = picUrl

    def getUrl(self):
        return self.Url

    def setUrl(self, url):
        self.Url = url


class NewsReply(BaseReply):
    """news(image and text) reply message class"""
    def __init__(self):
        super(NewsReply, self).__init__()
        self.ArticleCount = 0
        self.Articles = []

    def getArticleCount(self):
        return self.ArticleCount

    def setArticleCount(self, articleCount):
        self.ArticleCount = articleCount

    def getArticles(self):
        return self.Articles

    def setArticles(self, articles):
        self.Articles = articles
