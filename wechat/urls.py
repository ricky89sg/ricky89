


from django.conf.urls import patterns, include, url
from .views import wechat

app = 'wechat'

urlpatterns = [
    #url(r'^archive', wechat.views.archive),
    url(r'^cool/', wechat.views.wechat),
]