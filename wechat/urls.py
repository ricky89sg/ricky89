


from django.conf.urls import patterns, include, url
from .views import wechat

urlpatterns = patterns('',
  url(r'^$', WeChat.as_view()),
)