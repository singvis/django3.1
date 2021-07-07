#!/usr/bin/env python3
#-*- coding:UTF-8 -*-

from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question,Choice
from django.http import Http404

from django.views import  generic

"""通用视图"""
class IndexView(generic.ListView):
    # model = Question
    template_name = 'polls/index.html'
    context_object_name = 'last_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    # context_object_name = 'question'
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


"""函数式视图"""
# def index(request):
#     last_question_list = Question.objects.order_by('pub_date')[:5]
#     print(last_question_list)
#     output = ','.join(q.question_text for q in last_question_list)
#
#     return render(request, 'polls/index.html', locals())
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', locals())
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # return HttpResponse('你正在查看问卷%s 的投票结果' % question_id)
#     return render(request, 'polls/results.html', locals())

def vote(request, question_id):
    question =  get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':'你没有选择正确的选项!'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))


