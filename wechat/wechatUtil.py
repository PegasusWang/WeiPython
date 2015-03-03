# -*- coding:utf-8 -*-
"""
# Author: Pegasus Wang (pegasuswang@qq.com, http://ningning.today)
# Created Time : Wed Feb 18 18:18:10 2015

# File Name: wechatUtil.py
# Description:

# :copyright: (c) 2015 by Pegasus Wang.
# :license: MIT, see LICENSE for more details.
"""

import hashlib
from lxml import etree


def checkSignature(request):
    """check signature.

    :param request: get method
    :return: if success return True else False
    """
    signature = request.GET.get(u'signature', None)
    timestamp = request.GET.get(u'timestamp', None)
    nonce = request.GET.get(u'nonce', None)
    token = u'pegasuswang'    # your wechat token

    tmplist = [token, timestamp, nonce]
    tmplist.sort()
    tmpstr = '%s%s%s' % tuple(tmplist)
    tmpstr = hashlib.sha1(tmpstr).hexdigest()

    if tmpstr == signature:
        return True
    else:
        return False


class MessageUtil(object):
    """MessageUtil has some methods to process message."""
    # request message types
    REQ_MESSAGE_TYPE_TEXT = u'text'
    REQ_MESSAGE_TYPE_IMAGE = u'image'
    REQ_MESSAGE_TYPE_VOICE = u'voice'
    REQ_MESSAGE_TYPE_VIDEO = u'video'
    REQ_MESSAGE_TYPE_LOCATION = u'location'
    REQ_MESSAGE_TYPE_LINK = u'link'
    REQ_MESSAGE_TYPE_EVENT = u'event'

    # event types
    EVENT_TYPE_SUBSCRIBE = u'subscribe'
    EVENT_TYPE_UNSUBSCRIBE = u'unsubscribe'
    EVENT_TYPE_SCAN = u'scan'
    EVENT_TYPE_LOCATION = u'LOCATION'
    EVENT_TYPE_CLICK = u'CLICK'

    # reply message types
    RESP_MESSAGE_TYPE_TEXT = u'text'
    RESP_MESSAGE_TYPE_IMAGE = u'image'
    RESP_MESSAGE_TYPE_VOICE = u'voice'
    RESP_MESSAGE_TYPE_VIDEO = u'video'
    RESP_MESSAGE_TYPE_MUSIC = u'music'
    RESP_MESSAGE_TYPE_NEWS = u'news'

    # message types
    MESSAGETYPE = [u'Image', u'Voice', u'Video', u'Music', u'Articles']

    @staticmethod
    def parseXml(request):
        """parse request post xml message.

        :param request: post request
        :return: dict of xml message
        """
        raw_xml = request.body.decode(u'UTF-8')
        xmlstr = etree.fromstring(raw_xml)
        dict_xml = {}
        for child in xmlstr:
            dict_xml[child.tag] = child.text.encode(u'UTF-8')    # note
        return dict_xml

    

    @staticmethod
    def class2xml(obj):
        """convert reply message class to xml.

        :param obj: reply message class' object
        :return: xml of the object
        """
        root = etree.Element(u'xml')
        for key, value in vars(obj).items():
            if key in MessageUtil.MESSAGETYPE:
                tmproot = etree.SubElement(root, key)
                if key == u'Articles':    # solve Article, it's special
                    for eachArticle in value:
                        etree.SubElement(tmproot, u'item')
                        for tmpkey, tmpvalue in vars(eachArticle).items():
                            tmpkey_ele = etree.SubElement(tmproot, tmpkey)
                            tmpkey_ele.text = etree.CDATA(unicode(tmpvalue))
                else:
                    for tmpkey, tmpvalue in vars(obj.__getattribute__(key)).items():
                        tmpkey_ele = etree.SubElement(tmproot, tmpkey)
                    if u'time' in tmpkey.lower() or u'count' in tmpkey.lower():
                        tmpkey_ele.text = unicode(tmpvalue)
                    else:    # CDATA tag for str
                        tmpkey_ele.text = etree.CDATA(unicode(tmpvalue))
            else:
                if u'time' in key.lower() or u'count' in key.lower():
                    etree.SubElement(root, key).text = unicode(value)
                else:
                    etree.SubElement(root, key).text = etree.CDATA(unicode(value))

        return etree.tostring(root, pretty_print=True, xml_declaration=False, encoding=u'utf-8')
