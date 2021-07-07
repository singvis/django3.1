# !/usr/bin/env python3
# -*- coding:UTF-8 -*-

import traceback

from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.http import JsonResponse, QueryDict
from django.shortcuts import render,reverse,HttpResponse, HttpResponseRedirect, get_object_or_404, Http404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from pure_pagination.mixins import PaginationMixin
# from .models import User
from .form import UserForm
# from .form import UsersForm, UserModelForm, UserUpdateModelForm
from .form import UsersForm, UserModelForm
from django.conf import settings
from .models import Userprofile
from django.contrib.auth import get_user_model

import logging

log = logging.getLogger('devops')

User = get_user_model()

"""FBV(Function Basic View)"""
# def useradd(request):
#     """
#     添加用户
#     """
#     # print(request.method)
#     msg = {}
#     if request.method == 'POST':
#         try:
#             data = request.POST.dict()
#             User.objects.get_or_create(**data)
#             msg = {'code': 0, 'res': '创建用户成功.'}
#             log.info('添加用户成功.')
#         except:
#             # msg = {'code':1, "res":"创建用户失败: %s" % traceback.format_exc() }
#             msg = {'code':1, "res":"创建用户失败"}
#             log.error("创建用户失败: %s" % traceback.format_exc())
#
#     return render(request,'users/useradd.html', {'msg':msg})

# def userdel(request, **kwargs):
#     """
#     删除用户
#     """
#     pk = kwargs.get('pk', '')
#     try:
#         user = User.objects.get(id=pk)
#     except User.DoesNotExist:
#         raise Http404
#
#     msg = {}
#     if request.method == 'POST':
#         try:
#             User.objects.filter(id=pk).delete()
#             msg = {'code': 0, 'res': '删除用户成功.'}
#         except:
#             msg = {'code': 1, "res": "删除用户失败: %s" % traceback.format_exc()}
#
#     return render(request, 'users/userdel.html', {'pk':pk, 'user':user,'msg':msg})

# def useredit(request, **kwargs):
#     """
#     编辑用户
#     """
#     pk = kwargs.get('pk', '')
#     user = get_object_or_404(User, pk=pk)
#     msg = {}
#     if request.method == 'POST':
#         try:
#             data = request.POST.dict()
#             User.objects.filter(id=pk).update(**data)
#             msg = {'code': 0, 'res': '更新用户成功.'}
#         except:
#             msg = {'code': 1, "res": "更新用户失败: %s" % traceback.format_exc()}
#
#     return render(request, 'users/useredit.html', {'user':user, 'msg':msg})
#
# def userlist(request):
#     """
#     查看用户
#     """
#     keyword = request.GET.get('keyword', '')
#     userlist = User.objects.all()
#     if keyword:
#         userlist = User.objects.filter(name__icontains=keyword)
#     return render(request, 'users/userlist.html', {'userlist':userlist, 'keyword':keyword})


"""通用视图"""
# class IndexView(View):
#     def get(self, request):
#         return HttpResponse('this is get method.')
#     def post(self, request):
#         return HttpResponse('this is post method.')
#     def put(self, request):
#         return HttpResponse('this is put method.')
#     def delete(self, request):
#         return HttpResponse('this is delete method.')

# class UserListView(View):
#     def get(self, request):
#         keyword = request.GET.get('keyword', '')
#         if keyword:
#             userlist = User.objects.filter(name__icontains=keyword)
#         userlist = User.objects.all()
#         return render(request, 'users/userlist.html', {'userlist':userlist, 'keyword':keyword}

# class UserListView(TemplateView):
#     template_name = 'users/userlist.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(UserListView, self).get_context_data(**kwargs)
#         print(kwargs)
#         context['userlist'] =  User.objects.all()
#         print(context)
#         return context

# class UserListView(ListView):
#     template_name = 'users/userlist.html'
#     model = User
#     context_object_name = 'userlist'
#     keyword = ''

#     def get_queryset(self):
#         """
#         过滤数据传给前端渲染。
#         """
#         # 拿到所有数据
#         queryset = super(UserListView, self).get_queryset()
#         # print('所有数据结果:', queryset)
#         self.keyword = self.request.GET.get('keyword', '')
#         # print('关键字:', self.keyword)
#         # 搜索查询,过滤数据
#         if self.keyword:
#             # 过滤name
#             queryset = queryset.filter(name__icontains=self.keyword)
#             # print('过滤后的数据:', queryset)
#         return queryset
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         """
#         搜索后返回过滤数据及搜索框内的关键字
#         """
#         context = super(UserListView, self).get_context_data(**kwargs)
#         context['keyword'] = self.keyword
#         # print('context结果:', context)
#         return context


# class Detail(DetailView):
#     template_name = 'users/userdetail.html'
#     model = User
#     context_object_name = 'user'


# class UserAddView(SuccessMessageMixin, CreateView):
#     template_name = 'users/useradd.html'
#     model = User
#     fields = {'name', 'password', 'sex'}
#     success_message = "%(name)s was created successfuly"
#
#     def get_success_url(self):
#         # print(self.request.POST)
#         if '_addanother' in self.request.POST:
#             return reverse('users:useradd')
#         return reverse('users:userlist')
#
#     def form_valid(self, form):
#     #     print(form.errors)
#         print('~~~~~~~~~~~~~~~')
#         return HttpResponseRedirect(self.get_success_url())
#
#     # def form_invalid(self, form):
#         # print(form)
#         # return self.render_to_response(self.get_context_data(form=form))
#
#
#     # def get_context_data(self, **kwargs):
#     #     context = super(UserAddView, self).get_context_data(**kwargs)
#     #     users = User.objects.all()
#     #     context['users'] = users
#     #     return context


# class UserUpdateView(SuccessMessageMixin, UpdateView):
#     template_name = 'users/useredit.html'
#     model = User
#     fields = {'name', 'password', 'sex'}
#     success_message = "%(name)s was update successfuly"
#
#     def get_success_url(self):
#         print(self.kwargs)
#         return reverse('users:detail', kwargs={'pk':self.kwargs['pk']})


# class UserDeleteView(DeleteView):
#     template_name = 'users/userdel.html'
#     model = User
#
#     def get_success_url(self):
#         return reverse('users:userlist')


# 原生表单，简介版本
# class FormView(View):
#     def get(self, request):
#         form = UsersForm()
#         # print(form)
#         return render(request, 'users/form.html', {'form':form})
#
#     def post(self, request):
#         form = UsersForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             name = form.cleaned_data['name']
#             print(name)
#         return render(request, 'users/form.html', {'form':form})


# class ModelFormView(View):
#     def get(self, request):
#         return render(request, 'users/useradd.html')
#
#     def post(self, request):
#         form = UserModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             name = form.cleaned_data['name']
#             print(name)
#         return render(request, 'users/useradd.html', {'form':form})

"""modelform"""
# class UserFormAdd(TemplateView):
#     """
#     添加用户
#     """
#     template_name = 'users/user_form.html'


# class UserFormList(ListView):
#     """
#     1、用户列表：支持搜索
#     2、用户添加：通过ModelForm验证
#     """
#     model = User
#     template_name = 'users/userform_list.html'
#     context_object_name = 'userlist'
#     keyword = ''
#
#     def get_queryset(self):
#         # 获取所有数据
#         queryset = super(UserFormList, self).get_queryset()
#         # print(1, queryset)
#         # 获取搜索框关键字
#         self.keyword = self.request.GET.get('keyword', '').strip()
#         if self.keyword:
#             # Q的"|"表示或，“&”表示与
#             queryset = queryset.filter(Q(name__icontains=self.keyword)|
#                                        Q(phone__icontains=self.keyword))
#             # print(2, queryset)
#         # 返回搜后后过滤的数据给context
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         """
#         增加搜索关键字，一起传到前端
#         """
#         context = super(UserFormList, self).get_context_data(**kwargs)
#         # print(3, context)
#         context['keyword'] = self.keyword
#         # print(4, context)
#         return context
#
#     def post(self, request):
#         userform = UserModelForm(request.POST)
#         if userform.is_valid():
#             try:
#                 print(userform.cleaned_data)
#                 data = userform.cleaned_data
#                 self.model.objects.create(**data)
#                 # userform.save()
#                 res = {'code':0, 'result':'添加用户成功'}
#
#             except:
#                 res = {'code': 1, 'result': '添加用户失败'}
#                 log.error('添加用户失败%s' % traceback.format_exc())
#         else:
#             print(userform.errors)
#             print(userform.errors.as_json())
#             res = {'code': 1, 'result': userform.errors}
#
#         return render(request, settings.JUMP_PAGE, {'res':res})


# class UserFormDetail(DetailView):
#     """
#     1、用户更新
#     2、用户删除
#     """
#     template_name = 'users/userform_detail.html'
#     model = User
#     context_object_name = 'user'
#
#     def post(self, request, **kwargs):
#         keyword = kwargs.get('pk', '')
#         user = self.model.objects.get(id=keyword)
#         # print(user)
#         userform = UserUpdateModelForm(request.POST, instance=user)
#         # print(userform)
#         if userform.is_valid():
#             # 方法1： 原始的方法
#             # data = request.POST.dict()
#             # data.pop('confirm_password')
#             # print(data)
#             # self.model.objects.filter(id=keyword).update(**data)
#
#             # 方法二：
#             # data = userform.cleaned_data
#             # data.pop('confirm_password')
#             # self.model.objects.filter(id=keyword).update(**data)
#
#             # 方法三：
#             # print(userform.cleaned_data)
#             userform.save()
#             res = {'code':0, 'next_url':reverse('users:userlist'), 'result':'更新用户成功.'}
#         else:
#             print(userform.errors)
#             res = {'code':1, 'next_url':reverse('users:userlist'), 'result':'更新用户失败.'}
#
#         return render(request, settings.JUMP_PAGE, {'res':res})
#
#
#
#     def delete(self, request, **kwargs):
#         """
#         通过postman或curl来模拟删除
#         curl -X delete "http://127.0.0.1:8000/users/detail/6/"
#         """
#         # pk = kwargs.get('pk', '')
#         try:
#             # 方法1：
#             # self.model.objects.filter(id=pk).delete()
#
#             # 方法2：
#             # print(self.get_object())
#             self.get_object().delete()
#
#             res = {'code':0, 'next_url':reverse('users:userlist'), 'result':'删除用户成功.'}
#         except:
#             log.error('delete user error：{}'.format(traceback.format_exc()))
#             res = {'code': 1, 'next_url': reverse('users:userlist'), 'result': '删除用户失败.'}
#
#         return JsonResponse(res, safe=True)


"""jQuery"""
# class UserFormAdd(TemplateView):
#     template_name = 'users/user_form.html'


# class UserFormList(ListView):
#     """
#     1、用户列表：支持搜索
#     2、用户添加：通过ModelForm验证
#     """
#     model = User
#     template_name = 'users/userform_list.html'
#     context_object_name = 'userlist'
#     keyword = ''
#
#     def get_queryset(self):
#         # 获取所有数据
#         queryset = super(UserFormList, self).get_queryset()
#         # print(1, queryset)
#         # 获取搜索框关键字
#         self.keyword = self.request.GET.get('keyword', '').strip()
#         if self.keyword:
#             # Q的"|"表示或，“&”表示与
#             queryset = queryset.filter(Q(name__icontains=self.keyword)|
#                                        Q(phone__icontains=self.keyword))
#             # print(2, queryset)
#         # 返回搜后后过滤的数据给context
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         """
#         增加搜索关键字，一起传到前端
#         """
#         context = super(UserFormList, self).get_context_data(**kwargs)
#         # print(3, context)
#         context['keyword'] = self.keyword
#         # print(4, context)
#         return context
#
#     def post(self, request):
#         """
#         创建用户
#         """
#         userform = UserModelForm(request.POST)
#         if userform.is_valid():
#             try:
#                 # print(userform.cleaned_data)
#                 # data = userform.cleaned_data
#                 # self.model.objects.create(**data)
#                 userform.save()
#                 res = {'code':0, 'next_url':reverse('users:userlist'), 'result':'添加用户成功'}
#
#             except:
#                 res = {'code': 1, 'next_url':reverse('users:userlist'), 'result': '添加用户失败'}
#                 log.error('添加用户失败%s' % traceback.format_exc())
#         else:
#             # print(userform.errors)
#             # print(userform.errors.as_json())
#             res = {'code': 1, 'next_url':reverse('users:userlist'),'result': userform.errors.as_json()}
#
#         return JsonResponse(res, safe=True)
#
#     def delete(self, request):
#         """
#         删除用户
#         """
#         print(request.body)
#         data = QueryDict(request.body).dict()
#         print(data)
#         pk = data.get('id')
#         try:
#             user = User.objects.filter(id=pk)
#             user.delete()
#             res = {'code':0, 'result':'删除用户成功'}
#         except:
#             log.error("delete user error:{}".format(traceback.format_exc()))
#             res = {'code': 1, 'result': '删除用户失败'}
#         return JsonResponse(res, safe=True)



# class UserFormDetail(DetailView):
#     """
#     1、用户更新
#     2、用户删除
#     """
#     template_name = 'users/userform_detail.html'
#     model = User
#     context_object_name = 'user'
#
#     def post(self, request, **kwargs):
#         keyword = kwargs.get('pk', '')
#         user = self.model.objects.get(id=keyword)
#         # print(user)
#         userform = UserUpdateModelForm(request.POST, instance=user)
#         # print(userform)
#         if userform.is_valid():
#             # 方法1： 原始的方法
#             # data = request.POST.dict()
#             # data.pop('confirm_password')
#             # print(data)
#             # self.model.objects.filter(id=keyword).update(**data)
#
#             # 方法二：
#             # data = userform.cleaned_data
#             # data.pop('confirm_password')
#             # self.model.objects.filter(id=keyword).update(**data)
#
#             # 方法三：
#             # print(userform.cleaned_data)
#             userform.save()
#             res = {'code':0, 'next_url':reverse('users:userlist'), 'result':'更新用户成功.'}
#         else:
#             # print(userform.errors)
#             res = {'code':1, 'next_url':reverse('users:userlist'), 'result':userform.errors}
#
#         return render(request, settings.JUMP_PAGE, res)
#
#
#
#     def delete(self, request, **kwargs):
#         """
#         通过postman或curl来模拟删除
#         curl -X delete "http://127.0.0.1:8000/users/detail/6/"
#         """
#         # pk = kwargs.get('pk', '')
#         try:
#             # 方法1：
#             # self.model.objects.filter(id=pk).delete()
#
#             # 方法2：
#             # print(self.get_object())
#             self.get_object().delete()
#
#             res = {'code':0, 'next_url':reverse('users:userlist'), 'result':'删除用户成功.'}
#         except:
#             log.error('delete user error：{}'.format(traceback.format_exc()))
#             res = {'code': 1, 'next_url': reverse('users:userlist'), 'result': '删除用户失败.'}
#
#         return JsonResponse(res, safe=True)


"""前端测试"""
# class CssView(TemplateView):
#     template_name = 'users/css.html'


# class JssView(TemplateView):
#     template_name = 'users/jss.html'

# class JqView(TemplateView):
#     template_name = 'users/jq.html'
#
#     def post(self, request, **kwargs):
#         print(self.request.POST)
#         res = {'code':0, 'errmsg':'添加用户成功'}
#         return JsonResponse(res, safe=True)

# class BsView(ListView):
#     template_name = 'users/bs.html'
#     model = User


"""全新用户系统"""
# 老师的版本

class UserAddView(SuccessMessageMixin, CreateView):
    """
    新增用户
    """
    template_name = 'users/form.html'
    model = User
    form_class = UserModelForm
    success_message = '%(username)s 用户添加成功!'

    def get_success_url(self):
        # print(self.request.POST)
        if "_addanother" in self.request.POST:
            return reverse('users:useradd')
        return reverse('users:userlist')

    def form_valid(self, form):
        """
        form.cleaned_data： 获取表单所有数据
        from.instance： 新增的用户对象(是一个类)
        """
        password = form.cleaned_data['password']
        form.instance.password = make_password(password)
        # print('form_valid', form.cleaned_data)
        # print(make_password(password))
        # print(type(form.instance), form.instance)
        return super(UserAddView, self).form_valid(form)

    def form_invalid(self, form):
        """
        form_invalid方法可以不用写，用于print表单报错.
        """
        # print('form_invalid', form.cleaned_data)
        # print(form.errors.as_json())
        return super(UserAddView, self).form_invalid(form)


class UserListView(PaginationMixin, ListView):
    """
    查看用户
    """
    template_name = 'users/userlist.html'
    model = User
    context_object_name = 'users'
    paginate_by = 10
    keyword = ''

    def get_queryset(self):
        """ 数据过滤, return过滤后的数据 """
        # 获取所有数据
        queryset = super(UserListView, self).get_queryset()
        # print(queryset)
        # 获取搜索框的关键字
        self.keyword = self.request.GET.get('keyword', '')
        if self.keyword:
            if self.keyword == '男':
                queryset = queryset.filter(sex=0)
                print(queryset)
            elif self.keyword == '女':
                queryset = queryset.filter(sex=1)
            else:
                queryset = queryset.filter(Q(username__icontains=self.keyword)|
                                           Q(cn_name__icontains=self.keyword)|
                                           Q(is_superuser__icontains=self.keyword)|
                                           Q(phone__icontains=self.keyword)|
                                           Q(is_active__icontains=self.keyword))
        else:
            pass
        return queryset

    def get_context_data(self, **kwargs):
        """传给前端的数据"""
        context = super(UserListView, self).get_context_data(**kwargs)
        # print(context)
        context['keyword'] = self.keyword
        return context


class UserEditView(SuccessMessageMixin, UpdateView):
    """"
    更新用户
    """
    template_name = 'users/form.html'
    model = User
    form_class = UserModelForm
    success_message = '%(username)s was update successfully'

    def get_success_url(self):
        # print(self.request.POST)
        if '_savedit' in self.request.POST:
            # print(self.object.pk)
            # 是一个ID
            return reverse('users:useredit', kwargs={'pk':self.object.pk})
        return reverse('users:userlist')


    def form_valid(self, form):
        new_password = form.cleaned_data['password']
        print(self.object)
        # 是一个用户
        self.object.set_password(new_password)
        self.object.save()
        return super(UserEditView, self).form_valid(form)



class UserDelView(DeleteView):
    """
    删除用户
    """
    model = User
    # template_name = 'users/user_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        pk = self.kwargs
        print(pk)
        try:
            self.get_object().delete()
            res = {"code": 0, "result": "删除用户成功"}
        except:
            log.error('delete user error：{}'.format(traceback.format_exc()))
            res = {"code": 1, "result": "删除用户失败"}
        return JsonResponse(res, safe=True)


# ------------------------------------------------------------------------


"""
class UserFormAddView(CreateView):
    template_name = 'users/userform.html'
    model = Userprofile
    fields = {'username', 'password', 'sex'}

    def get_success_url(self):
        return reverse('users:userlist')

    def post(self, request, *args, **kwargs):
        userform = UserModelForm(request.POST)
        # print(userform)
        if userform.is_valid():
            try:
                data = userform.cleaned_data
                # self.model.objects.create(**data)
                print(data)
                userform.save()
                res = {'code': 0, 'result': '添加用户成功'}
            except:
                res = {'code': 1, 'result': '添加用户失败'}
        else:
            res = {'code': 1, 'result': userform.errors.as_json()}

        return render(request, settings.JUMP_PAGE,  {'res':res})


class UserFormListView(ListView):
    template_name = 'users/userlist_form.html'
    model = Userprofile
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super(UserFormListView, self).get_queryset()
        queryset = queryset.exclude(username='admin')
        return queryset

    def post(self, request):
        userform = UserModelForm(request.POST)
        print(userform)
        if userform.is_valid():
            try:
                print('开始打印成功消息0...')
                userform.save()
                res = {'code': 0, 'next_url': reverse('users:userlist'), 'result': '添加用户成功'}
            except:
                print('开始打印错误消息1...')
                res = {'code':1, 'next_url':reverse('users:userlist'), 'result':'添加用户失败'}
                log.error('添加用户失败:{}'.format(traceback.format_exc()))
        else:
            res = {'code': 1, 'next_url': reverse('users:userlist'), 'result': userform.errors.as_json()}
            print('开始打印错误消息2...')
            print(userform.errors.as_json())
        return JsonResponse(res, safe=True)


class UserFormEditView(UpdateView):
    pass


class UserFormDelView(DeleteView):
    pass
    
"""