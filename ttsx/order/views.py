# coding=utf-8
import datetime
from django.shortcuts import render

# Create your views here.
from cart.models import CartInfo
from order.models import OrderDetail, OrderInfo
from user.models import UserInfo


def place_order(request):
    cart_list = []
    total_one_list = []
    total_all = 0
    cart_ids = request.POST.getlist('ischose')  # 获取购物车主键id

    order = OrderInfo()  # 创建一个订单对象，用来存订单总计
    order.id = datetime
    for cart_id in cart_ids:
        cart = CartInfo.objects.get(pk=int(cart_id))
        od = OrderDetail()
        od.ogprice = cart.cgood.gprice  # 每个的单价
        od.ogcount = cart.ccount  # 个数

        total_one = cart.cgood.gprice*cart.ccount  # 计算每个的小计
        total_all += total_one  # 计算总计
        cart_list.append(cart)
        total_one_list.append({'total_one': total_one,'cart':cart})
    order.ototalprice = total_all + 10
    uid = int(request.session.get('uid'))  # 获取用户id
    user = UserInfo.objects.get(pk=uid)
    context = {'title': '提交订单', 'head': 1, 'logo_search': 2, 'user': user,
               'total_one_list': total_one_list, 'total_all': total_all,'fin_pay': fin_pay,
               }
    # 存入订单库后，将购物车中已提交订单的商品删掉

    ogprice
    return render(request, 'place_order.html', context)
