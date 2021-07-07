#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django import template

register = template.Library()

@register.filter
def test(x,y):
    return int(x) + int(y)
