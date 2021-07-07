#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.urls import path, re_path
from .views import *

app_name = 'users'
urlpatterns = [
    # path('useradd/', useradd, name='useradd'),
    # re_path('userdel/(?P<pk>[0-9]+)?/', userdel, name='userdel'),
    # re_path('useredit/(?P<pk>[0-9]+)?/', useredit, name='useredit'),
    # path('userlist/', userlist, name='userlist'),
    # 通用视图
    # path('index/', IndexView.as_view(), name='index'),
    # path('userlist/', UserListView.as_view(), name='userlist'),
    # DetailView
    # re_path('detail/(?P<pk>[0-9]+)?/', Detail.as_view(), name='detail' ),
    # CreateView
    # path('useradd/', UserAddView.as_view(), name='useradd'),
    # UpdateView
    # re_path('useredit/(?P<pk>[0-9]+)?/', UserUpdateView.as_view(), name='useredit'),
    # DeleteView
    # re_path('userdel/(?P<pk>[0-9]+)?/', UserDeleteView.as_view(), name='userdel'),

    # modelform
    # path('useradd/', UserFormAdd.as_view(), name='useradd'),
    # path('userlist/', UserFormList.as_view(), name='userlist'),
    # re_path('detail/(?P<pk>[0-9]+)?/', UserFormDetail.as_view(), name='detail' ),

    # jQuery版本
    # path('useradd/', UserFormAdd.as_view(), name='useradd'),
    # path('userlist/', UserFormList.as_view(), name='userlist'),
    # re_path('detail/(?P<pk>[0-9]+)?/', UserFormDetail.as_view(), name='detail' ),

    # 表单
    # path('form/', FormView.as_view(), name='form'),
    # path('modelform/', ModelFormView.as_view(), name='modelform'),

    # 前端测试
    # path('css/', CssView.as_view(), name='css'),
    # path('js/', JssView.as_view(), name='jss'),
    # path('jq/', JqView.as_view(), name='jq'),
    # path('bs/', BsView.as_view(), name='bs'),

    # 全新用户系统(前端美化)
    # 老师版本
    path('userlist/', UserListView.as_view(), name='userlist'),
    path('useradd/', UserAddView.as_view(), name='useradd'),
    re_path('useredit/(?P<pk>[0-9]+)?/', UserEditView.as_view(), name='useredit'),
    re_path('userdel/(?P<pk>[0-9]+)?/', UserDelView.as_view(), name='userdel'),

    # 自己改版
    # path('useradd/', UserFormAddView.as_view(), name='useradd'),
    # path('userlist/', UserFormListView.as_view(), name='userlist'),
    # re_path('useredit/(?P<pk>[0-9]+)?/', UserFormEditView.as_view(), name='useredit'),
    # re_path('userdel/(?P<pk>[0-9]+)?/', UserFormDelView.as_view(), name='userdel'),
]