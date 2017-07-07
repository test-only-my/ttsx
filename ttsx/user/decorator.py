# coding=utf-8
# 装饰器，用来判断是否已经登录，验证在登录后的状态才能显示的页面
from django.shortcuts import redirect


def islogin(func):
    def decorator_func(request,*args,**kargs):
        if request.session.get('uid'):
            return func(request)
        else:
            return redirect('/user/login/')
    return decorator_func
