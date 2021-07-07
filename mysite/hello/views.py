#!/usr/bin/env python3
#-*- coding:UTF-8 -*-


from django.http import QueryDict
from django.shortcuts import render, HttpResponse
from .models import User

# def index(request):
#     # return render(request, 'hello/index.html')
#     """
#     1.普通URL
#     http://127.0.0.1:8000/?year=2021&month=05
#     """
#     # print(request.GET)
#     year = request.GET.get('year', '')
#     month = request.GET.get('month', '')
#     return HttpResponse("{} year {} month.".format(year, month))

# def index(request, year, month):
#     """
#     2.位置参数
#     http://127.0.0.1:8000/2021/05/
#     """
#     return HttpResponse("{} year {} month.".format(year, month))

# def index(request, **kwargs):
#     """
#     3.关键字参数
#     http://127.0.0.1:8000/2021/05/
#     """
#     print(kwargs)
#     year = kwargs.get('year')
#     month = kwargs.get('month')
#     return HttpResponse("{} year {} month.".format(year, month))

# def index(request):
#     """
#     GET or POST
#     """
# print('method:', request.method)
# print('scheme:', request.scheme)
# print('body:', request.body)
# print('headers', request.headers)
# print('path', request.path)
# print('META', request.META)
# print('GET', request.GET)
# year = request.GET.get('year', '')
# month = request.GET.get('month', '')

# if request.method == 'POST':
#     print(request.method)
#     print(request.body)
#     print(request.POST)
#     print(QueryDict(request.body).dict())
#     year = request.POST.get('year', '')
#     month = request.POST.get('month', '')
# # return HttpResponse("Hello, Django.")
# return HttpResponse("{} year {} month.".format(year, month))


# def index(request):
#     name = 'hello,django.'
#     books = ['python', 'java', 'Go']
#     userlist = [{'name':'Jack', 'age':18}]
#     return render(request, 'hello/index.html', {'userlist':userlist})

# def index(request):
#     userlist = [{'name':'Jack', 'name_cn':'杰克', 'age':18},
#                 {'name':'Tony', 'name_cn':'托尼', 'age':20}]
#     messages = 'Life is short, You need Python.'
#     messages = ['python', 'django', 'Go']
#     return render(request, 'hello/userlist.html', {'userlist':userlist, 'messages':messages})

def index(request):
    users = User.objects.all()
    return render(request, 'hello/userlist.html', {'users':users})
