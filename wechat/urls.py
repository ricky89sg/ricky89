
from django.conf.urls import include, url
from .views import wechat

app = 'wechat'

urlpatterns = [
    #url(r'^archive', wechat.views.archive),
    #url(r'^$', wechat.views.wechat),
	url(r'^$', wechat),    
]