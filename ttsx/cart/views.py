# coding=utf-8
from django.shortcuts import render

from cart.models import CartInfo
from user import decorator
from django.http import JsonResponse
# Create your views here.
@decorator.islogin
def cart(request):
    context = {'title':'购物车','head':1,'logo_search':2}
    return render(request,'cart.html',context)

# 加入购物车之前，判断是否已经登录
def islogin(request):
    if request.session.has_key('uid'):
        context = {'flag1':1}
    else:
        context = {'flag1':0}
    return JsonResponse(context)

# 添加购物车
def add(request):
    try:
        uid = int(request.session.get('uid'))
        gid = int(request.GET.get('gid'))
        gcount = int(request.GET.get('gcount', 1))
        cart = CartInfo.objects.filter(cuser_id=uid,cgood_id=gid)
        if len(cart)==1:
            cart.ccount+=gcount
        else:
            cart = CartInfo()
            cart.cuser_id = uid
            cart.cgood_id = gid
            cart.ccount = gcount
            cart.save()
        context = {'result':1,'gcount':gcount}
    except:
        context = {'result':0,'gcount':0}
    return JsonResponse(context)