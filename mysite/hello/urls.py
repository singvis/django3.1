#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.urls import path,re_path
from .views import index

app_name = 'hello'
urlpatterns = [
    # 1.普通URL
    path('', index, name='index'),
    # 2.位置参数
    # re_path('([0-9]{4})/([0-9]{2})/', index),
    # 3.关键字参数
    # re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', index),
    path('userlist/', index, name='userlist'),
]