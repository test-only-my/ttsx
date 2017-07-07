# coding=utf-8
from django.shortcuts import render

# Create your views here.

# 首页
from goods.models import *


def index(request):
    list_dic = []  # [{key1:[],key2:[]}]最后是这种格式
    # user = UserInfo.objects.filter(id=request.session.get('uid'))
    type_list = GoodType.objects.all()  # 所有类型取出来
    for t in type_list:
        top_goods = t.goodinfo_set.order_by('-gclick')[0:4]  # 点击量最高的商品
        new_goods = t.goodinfo_set.order_by('-id')[0:4]  # 最新的商品
        list_dic.append({'top_goods':top_goods,'new_goods':new_goods,'t':t})  # 将两个列表分别存在字典里，每个键对应一个列表

    context = {'title': '首页', 'head': 1, 'logo_search': 1,'list_dic':list_dic,'type_list':type_list}
    return render(request, 'index.html', context)

def list(request):
    return render(request,'list.html')
