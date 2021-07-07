#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.urls import path
from . import views

app_name = 'polls'
# FBV方式
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/result/', views.results, name='result'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

# 通用视图：CBV
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]