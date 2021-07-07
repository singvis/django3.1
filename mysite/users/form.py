#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django import forms
from django.contrib.auth import get_user_model
import re

User = get_user_model()

# 原生表单验证各种表单类型及定义
class UserForm(forms.Form):
    name = forms.CharField(max_length=32, required=True)
    password = forms.CharField(max_length=32, required=True)
    sex = forms.CharField(max_length=10, required=False)

# 原生表单渲染前端，简介版本
class UsersForm(forms.Form):
    name = forms.CharField(max_length=10, required=True)
    password = forms.CharField(max_length=12, required=True, widget=forms.PasswordInput)

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User    # 与model建立了依赖关系，即按照model中的字段类型验证
        fields = "__all__"  # 根据model定义的类型，验证所有列的属性
        # fields = ['name', 'password']     # 验证指定列
        # exclude = ['sex']     # 排除那些列

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone_re = r'^1([3-9])[0-9]{9}$'
        p = re.compile(phone_re)
        if p.match(phone):
            return phone
        else:
            # ValidationError自定义比表单错误
            raise forms.ValidationError("手机号码非法", code='invalid')


class UserUpdateModelForm(forms.ModelForm):
    # 新增字段，用于做密码确认
    confirm_password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = '__all__'

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        phone_re = r'^1([3-9])[0-9]{9}$'
        p = re.compile(phone_re)
        if p.match(phone):
            return phone
        else:
            # ValidationError自定义比表单错误
            raise forms.ValidationError("手机号码非法", code='invalid')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('两次密码不一致!', code='password_mismatch',)
        return confirm_password


# 全新系统
class UserModelForm(forms.ModelForm):
    # 新增确认密码字段，用于两次密码作比较
    # 该字段不用写入数据库
    confirm_password = forms.CharField(required=True)

    class Meta:
        # 与model建立了依赖关系，即按照model中的字段类型验证
        model = User
        # 根据model定义的类型，验证所有列的属性
        fields = ('username', 'cn_name', 'password', 'sex', 'phone')
        # fields = ['username', 'password']     # 验证指定列
        # exclude = ['sex']     # 排除那些列

    def clean_phone(self):
        # clean_字段名，该方法用于验证字段，自定义条件
        phone = self.cleaned_data['phone']
        if phone:
            phone_re = re.match("^1[35789][0-9]{9}$", phone)
            # print(phone_re)
            if phone_re:
                return phone
            else:
                raise forms.ValidationError("手机号码非法")
        # 方法2：
        # if self.cleaned_data['phone']:
            # phone_re = r'^1([3-9])[0-9]{9}$'
            # p = re.compile(phone_re)
            # if p.match(phone):
            #     return phone
        else:
            # ValidationError自定义表单错误
            raise forms.ValidationError("这个字段是必填项")

    def clean_confirm_password(self):
        """
        用于比较两次输入的密码
        """
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('两次密码不一致!')
        # return confirm_password