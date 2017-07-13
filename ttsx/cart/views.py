# coding=utf-8
from django.db.models import Sum
from django.shortcuts import render

from cart.models import CartInfo
from user import decorator
from django.http import JsonResponse
# Create your views here.
@decorator.islogin
def cart(request):
    uid = int(request.session.get('uid'))
    cart_goods = CartInfo.objects.filter(cuser_id=uid)
    context = {'title':'购物车','head':1,'logo_search':2,'cart_goods':cart_goods}
    return render(request,'cart.html',context)

# 加入购物车之前，判断是否已经登录
def islogin(request):
    if request.session.has_key('uid'):
        context = {'flag1':1}
        context['uid'] = request.session.get('uid')
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
        # 如果购物车中有这个商品，就只是数量增加count，否则新建一个商品，填入count
        if len(cart)==1:
            cart[0].ccount+=gcount
            cart[0].save()
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

def count1(request):
    uid = int(request.session.get('uid'))
    # 因为聚合函数返回的是字典样式{"ccount__sum": 60}，并不是个值，所以需要get取出来
    sum_count = CartInfo.objects.filter(cuser_id=uid).aggregate(Sum('ccount')).get('ccount__sum')
    return JsonResponse({'sum_count':sum_count})

def save_count(request):
    try:
        id = int(request.GET.get('id'))
        num = int(request.GET.get('num'))
        cart = CartInfo.objects.get(pk=id)
        cart.ccount = num
        cart.save()
        context = {'ok': 1}
    except:
        context = {'ok':0}
    return JsonResponse(context)

def del_cart(request):
    try:
        id = int(request.GET.get('id'))
        cart = CartInfo.objects.get(pk=id)
        cart.delete()
        context = {'ok':1}
    except:
        context = {'ok':0}
    return JsonResponse(context)