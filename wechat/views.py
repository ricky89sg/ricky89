## coding=utf-8


import hashlib 
from django.http import HttpResponse 
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


wechat_token = '909363995'  # 改成你自己设置的 token 就可以啦.
@csrf_exempt
def wechat(request):
    if request.method == "GET":    # 确定微信发来了 GET, 得到所有参数
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
    	token = wechat_token 
        range_dict = [token, timestamp, nonce] # 做成一个字典
        range_dict.sort()  # 把字典排序
        range_str = "%s%s%s" % tuple(range_dict)  # 转换成元祖
        range_str = hashlib.sha1(range_str).hexdigest() 然后用 hashlib 加密一下.

        if range_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("weixin  index")  # 随便返回点儿什么

    elif request.method == "POST":
		# do something about POST here
		str_xml = request.body.decode('utf-8')    #use body to get raw data
		xml = etree.fromstring(str_xml)            
		toUserName = xml.find('ToUserName').text
		fromUserName = xml.find('FromUserName').text
		createTime = xml.find('CreateTime').text
		msgType = xml.find('MsgType').text
		content = xml.find('Content').text   #获得用户所输入的内容
		msgId = xml.find('MsgId').text
		return render(request, 'reply_text.xml',
			{
				'toUserName': fromUserName,
				'fromUserName': toUserName,
				'createTime': time.time(),
				'msgType': msgType,
				'content': content,
			},
			content_type = 'application/xml'
		)
