#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.db import models
from django.utils import timezone
import datetime

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         # return bool
#         now = timezone.now()
#         return now >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#     was_published_recently.admin_order_field = 'pub_date'
#     # 显示√和×图标
#     was_published_recently.boolean = True
#     was_published_recently.short_description = '是不是最近发布的问卷'


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text
