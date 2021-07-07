#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.db import models

class User(models.Model):
    SEX = ((1, '男'),
           (2, '女'))
    name = models.CharField(max_length=32, help_text='用户名')
    password = models.CharField(max_length=32, help_text='密码')
    sex = models.IntegerField(choices=SEX, null=True, blank=True)

    def __str__(self):
        return self.name
