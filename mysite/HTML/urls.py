#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.urls import path
from . import views

app_name = 'HTML'
urlpatterns = [
    path('', views.HtmlView.as_view(), name='html'),
]