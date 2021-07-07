from django.shortcuts import render
from .models import User



def add(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        img = request.FILES.get('img')
        introduce = request.FILES.get('introduce')
        # print(username, img, introduce)
        user = User(username=username, img=img, introduce=introduce)
        user.save()

    return render(request,  'uploads/add.html', locals())

def detail(request):
    user_list = User.objects.all()
    return render(request, 'uploads/detail.html', locals())
