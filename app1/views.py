from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    print('这是第一个视图')

    return HttpResponse('success')


def demo(request):

    print('这是dev分支上的代码')

    return HttpResponse('成功了')

def user(request):
    print('this is user')

    return HttpResponse('访问到了user视图')