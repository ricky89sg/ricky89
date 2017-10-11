# -*- coding: utf-8 -*-

from __future__ import unicode_literals
 
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
 
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
'''
import hashlib
import json
from lxml import etree
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
#from auto_reply.views import auto_reply_main # 修改这里
 
WEIXIN_TOKEN = '909363995'
'''
''' 
@csrf_exempt
def wechat(request):
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("weixin  index")
    else:
    	str_xml = request.body.decode('utf-8')    #use body to get raw data
        xml = etree.fromstring(str_xml)    #进行XML解析
        toUserName = xml.find('ToUserName').text
        fromUserName = xml.find('FromUserName').text
        #createTime = xml.find('CreateTime').text
        msgType = xml.find('MsgType').text
        content = xml.find('Content').text   #获得用户所输入的内容
        msgId = xml.find('MsgId').text

        return render(request, 'text_reply.xml',
                      {'toUserName': fromUserName,
                       'fromUserName': toUserName,
                       'createTime': time.time(),
                       'msgType': msgType,
                       'content': content,
                       },
                       content_type = 'application/xml',
                       #content_type = 'text/xml',
        )

        regq = re.compile(r'\/.*$')
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        #response_xml = auto_reply_main(request_xml)# 修改这里

        t = loader.get_template('text.xml')
        c = {'toUser': toUser, 'fromUser': fromUser,'nowtime': nowtime, 'content': content}
        return HttpResponse(t.render(c))
    	'''

        #return HttpResponse(response_xml)
        




 
 
WECHAT_TOKEN = '909363995'
AppID = 'wxc5ed30581ee27ebb'
AppSecret = '4153eb9a9048eac21212646a91587fd3'
 
# 实例化 WechatBasic
wechat_instance = WechatBasic(
    token=WECHAT_TOKEN,
    appid=AppID,
    appsecret=AppSecret
)
 
@csrf_exempt
def wechat(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')
 
        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')
 
        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")
 
 
    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')
 
    # 获取解析好的微信请求信息
    message = wechat_instance.get_message()
 
    # 关注事件以及不匹配时的默认回复
    response = wechat_instance.response_text(
        content = (
            'Hello, world!\n'
            ))
    '''
    if isinstance(message, TextMessage):
        # 当前会话内容
        content = message.content.strip()
        if content == '功能':
            reply_text = (
                    '目前支持的功能：\n1. 关键词后面加上【教程】两个字可以搜索教程，'
                    '比如回复 "Django 后台教程"\n'
                    '2. 回复任意词语，查天气，陪聊天，讲故事，无所不能！\n'
                    '还有更多功能正在开发中哦 ^_^\n'
                    '【<a href="http://www.ziqiangxuetang.com">自强学堂手机版</a>】'
                )
        elif content.endswith('教程'):
            reply_text = '您要找的教程如下：'
    
        response = wechat_instance.response_text(content=reply_text)
    '''
    return HttpResponse(response, content_type="application/xml")




