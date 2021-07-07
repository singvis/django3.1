#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

class IndexView(TemplateView):
    # def get(self, request):
    #     return render(request, 'index.html')
    template_name = 'index1.html'
