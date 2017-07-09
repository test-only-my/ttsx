# coding=utf-8
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import response
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

def list(request,tid,pIndex):
    t = GoodType.objects.filter(pk=int(tid))[0]
    # 根据index页面地址栏传过来的type的id，查出这个类型的商品
    # 最新两个商品
    new_list = GoodInfo.objects.filter(gtype=int(tid.decode('utf8'))).order_by('-id')[0:2]
    # 全部这个类型的商品，按id倒序排序
    all_list = GoodInfo.objects.filter(gtype=int(tid.decode('utf8'))).order_by('-id')
    # 分页显示，每页15个
    p = Paginator(all_list,15)
    # 返回页码列表
    index_list = p.page_range
    # 当前页码
    # pIndex = p.page(pIndex).number
    # 获取当前页的数据,表示要拿第几页
    now_page = p.page(int(pIndex.decode('utf8')))
    context = {'logo_search':1,'t':t,
               'new_list':new_list,'now_page':now_page,
               'index_list':index_list}
    return render(request,'list.html',context)

def detail(request,tid,gid):

    # print(tid,gid)
    t = GoodType.objects.filter(id=int(tid))
    # 根据id去查找要显示详情的商品
    good = GoodInfo.objects.filter(Q(id=int(gid)) & Q(gtype=int(tid)))
    if good:
        # 最新商品推荐展示两个
        new_list = GoodInfo.objects.filter(gtype=int(tid.decode('utf8'))).order_by('-id')[0:2]
        context = {'head':1,'logo_search':1,'t':t[0],'good':good[0],'new_list':new_list}
        # 将浏览的商品计入cookie
        response = render(request,'detail.html',context)
        if request.COOKIES.has_key('see_goods'):
            see_goods = request.COOKIES['see_goods']
            see_index = str(see_goods).find(str(good[0].id)+"|",0,len(see_goods))
            if see_index!=-1:
                see_goods = see_goods.replace(str(good[0].id)+"|",'')
            # elif see_index==0:
            #     see_goods.replace(str(good[0].id)+"|",'')
            else:
                pass
            str1 = str(good[0].id)+"|"
            see_goods += str1
            response.set_cookie('see_goods',see_goods)
        else:
            response.set_cookie('see_goods',str(good[0].id)+"|")
        return response
    else:
        return render(request, '404.html')