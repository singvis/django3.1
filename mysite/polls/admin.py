#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.contrib import admin

# from .models import Question,Choice
#
#
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     # 扩展框
#     extra = 3
#
# class QuestionAdmin(admin.ModelAdmin):
#     # 显示字段
#     list_display = ['question_text', 'pub_date', 'was_published_recently']
#     # 增加过滤字段
#     list_filter = ['pub_date']
#     # 增加搜索框
#     search_fields = ['question_text']
#     # 分页
#     list_per_page = 2
#     # fields = ['pub_date', 'question_text']
#
#     fieldsets = [
#         ('question_text', {'fields':['question_text']}),
#         ('date information', {'fields':['pub_date']}),
#     ]
#     inlines = [ChoiceInline]
#
# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)