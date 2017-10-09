#coding:utf-8

import hashlib
import json
from lxml import etree
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
#from auto_reply.views import auto_reply_main # 修改这里
 
WEIXIN_TOKEN = '909363995'
 
@csrf_exempt
def wechat(request):
    """
    所有的消息都会先进入这个函数进行处理，函数包含两个功能，
    微信接入验证是GET方法，
    微信正常的收发消息是用POST方法。
    """
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
        toUserName = xml.find('ToUserName').text
        fromUserName = xml.find('FromUserName').text
        #createTime = xml.find('CreateTime').text
        #msgType = xml.find('MsgType').text
        content = xml.find('Content').text   #获得用户所输入的内容
        msgId = xml.find('MsgId').text

        return render(request, 'text_reply.xml',
                      {'toUserName': fromUserName,
                       'fromUserName': toUserName,
                       'createTime': time.time(),
                       'msgType': 'text',
                       'content': content,
                       },
                       content_type = 'application/xml',
                       #content_type = 'text/xml',
        )
        '''
        regq = re.compile(r'\/.*$')
    	'''
    	'''
        xml_str = smart_str(request.body)
        request_xml = etree.fromstring(xml_str)
        #response_xml = auto_reply_main(request_xml)# 修改这里
        '''
    	'''
        t = loader.get_template('text.xml')
        c = {'toUser': toUser, 'fromUser': fromUser,'nowtime': nowtime, 'content': content}
        return HttpResponse(t.render(c))
    	'''

        #return HttpResponse(response_xml)
        







