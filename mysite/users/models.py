#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.db import models
from django.contrib.auth.models import AbstractUser


# class User(models.Model):
#     SEX = ((1, '男'),
#            (2, '女'))
#     name = models.CharField(max_length=10, help_text='用户名')
#     phone = models.CharField(max_length=11, default='13800000001', help_text='手机')
#     password = models.CharField(max_length=64, help_text='密码')
#     sex = models.IntegerField(choices=SEX, null=True, blank=True)
#
#     def __str__(self):
#         return self.name

class Userprofile(AbstractUser):
    SEX_CHOICE = (
        (0, '男'),
        (1, '女'),
    )
    cn_name = models.CharField('中文名', max_length=128)
    phone = models.CharField('手机', max_length=11, null=True, blank=True)
    sex = models.IntegerField(choices=SEX_CHOICE, null=True, blank=True)


    class Meta:
        verbose_name = '用户信息'

    def __str__(self):
        return self.username


