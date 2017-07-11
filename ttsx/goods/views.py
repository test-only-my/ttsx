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

    context = {'title': '首页', 'head': 1, 'logo_search': 1,'list_dic':list_dic,'type_list':type_list,'kind1':str(0)}
    return render(request, 'index.html', context)

def list(request,tid,pIndex):
    kind = request.GET.get('kind','0')
    order = request.GET.get('order','1')
    t = GoodType.objects.filter(pk=int(tid))[0]
    # 根据index页面地址栏传过来的type的id，查出这个类型的商品
    # 最新两个商品
    new_list = GoodInfo.objects.filter(gtype=int(tid.decode('utf8'))).order_by('-id')[0:2]
    # 全部这个类型的商品，按id倒序排序
    all_list = GoodInfo.objects.filter(gtype=int(tid.decode('utf8')))
    # 默认
    if kind == '0':
        all_list = all_list.order_by('-id')
        # 价格
    elif kind == '1':
        if order == '1':
            all_list = all_list.order_by('gprice')
            order = -1
        elif order == '-1':
            all_list = all_list.order_by('-gprice')
            order = 1
        # 人气,点击量
    elif kind == '2':
        if order == '1':
            all_list = all_list.order_by('gclick')
            order = -1
        elif order == '-1':
            all_list = all_list.order_by('-gclick')
            order = 1
    # 分页显示，每页15个
    p = Paginator(all_list,15)
    # 返回页码列表
    index_list_all = p.page_range
    # 获取当前页的数据,表示要拿第几页
    now_page = p.page(int(pIndex.decode('utf8')))
    index_list = []
    # ...3 4 5 6 7 ...页码做成这种格式，在后台判断好直接返回给页面，由页面遍历产生
    if len(index_list_all) <= 5:
        index_list = index_list_all
    elif now_page.number<=2:
        index_list = [1,2,3,4,5]
    elif p.num_pages-now_page.number<=2:
        index_list = p.page_range[-5:]
    else:
        index_list = [now_page.number-2,now_page.number-1,now_page.number,now_page.number+1,now_page.number+2]
        # index_list.insert(0, '...')
        # index_list.append('...')
    context = {'head':1,'logo_search':1,'t':t,
               'new_list':new_list,'now_page':now_page,'p':p,'kind':kind,'order':order,
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
        # 在取cookie时如果没有，就设置默认值为‘’,按照','去分割，得到列表
        see_goods = request.COOKIES.get('see_goods','').split(',')
        # 如果商品存在于浏览记录中，就把这个记录删掉，后面把这次浏览的记录插入到0的位置
        if str(gid) in see_goods:
            see_goods.remove(str(gid))
        # 将刚刚浏览的商品id插入到列表0的位置
        see_goods.insert(0,gid)
        # 只留5个，一旦超过就把最后一个pop
        if len(see_goods)>5:
            see_goods.pop()
        response.set_cookie('see_goods',','.join(see_goods))
        # 每点击一次进入详情页，点击量就+1
        good[0].gclick = int(good[0].gclick)+1
        good[0].save()
        return response
    else:
        return render(request, '404.html')

