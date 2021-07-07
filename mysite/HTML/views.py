# --*-- coding=utf-8 --*--


from django.shortcuts import render,reverse
from django.views.generic import View,TemplateView
import os

class HtmlView(TemplateView):
    template_name = 'HTML/test.html'
    def post(self, request):
        # print(request.POST)
        # data = request.POST.dict
        # print(data)
        # 方法1：获取多选框的一键多值
        # hobby = request.POST.getlist('hobby', '')
        # 方法2：字典解析式
        data = dict((k, ','.join(v)) for k, v in dict(request.POST).items())
        print(data)
        file = request.FILES.get('file', None)
        if file:
            f = open(os.path.join('mysite/media/images/', file.name), 'wb')
            for line in file.chunks():
                f.write(line)
            f.close()
        return render(request, 'HTML/test.html')