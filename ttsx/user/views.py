# coding=utf-8
import re
from datetime import date, datetime

from django.http import HttpResponse,JsonResponse, response
from django.shortcuts import render,redirect
from hashlib import sha1
# Create your views here.
from django.utils.timezone import now

from user.models import UserInfo


# 首页
def index(request):
    context = []
    return render(request, 'index.html')


# user用户模块
# 注册页面展示
def register(request):
    # head为0,不显示顶栏
    context = {'title': '注册','head':0}
    return render(request, 'user/register.html', context)

# 注册判重校验
def register_again(request,args):
    uname = args.get('user_name')
    valible = UserInfo.objects.filter(uname=uname)
    context = {'valible': valible}
    # 判断该用户是否已存在
    return JsonResponse(context)

# 注册过程校验
def register_check(request):
    # head为0,不显示顶栏
    # context = {}
    # context['head'] = 0

    args = request.POST
    uname = args.get('user_name')
    passwd = args.get('pwd')
    passwd_confirm = args.get('cpwd')
    uemail = args.get('email')
    allow = args.get('allow')
    # re1 = '^[a - z0 - 9][\w\.\-]*@[a - z0 - 9\-]+(\.[a - z]{2, 5}){1, 2}$'
    re1='^[a - z0 - 9]'
    context = {
        'title':'注册',
        'uname':uname,
        'passwd':passwd,
        'passwd_confirm':passwd_confirm,
        'uemail':uemail
    }
    if len(uname) < 5 or len(uname) > 20:
        context['error_name'] = '请输入5-20个字符的用户名'
        return render(request,'user/register.html',context)
    elif len(passwd) < 8 or len(passwd) > 20:
        context['error_pwd'] = '密码最少8位，最长20位'
        return render(request,'user/register.html',context)
    elif re.match(re1,uemail) == None:
        context['error_email'] = '你输入的邮箱格式不正确'
        return render(request,'user/register.html',context)
    elif allow != 'on':
        context['error_allow'] = '请勾选同意'
        return render(request, 'user/register.html', context)
    else:
        user = UserInfo()
        user.username = uname
        user.email = uemail
        # 密码加密
        s1 = sha1()
        s1.update(passwd)# python3中需要把passwd先encode
        upwd_sha1 = s1.hexdigest()
        user.passwd = upwd_sha1
        user.save()
        return redirect('/login/')

# 登录页面展示
def login(request):
    # 如果cookie中有值，进入login页面，直接拿到显示在页面上

    uname = request.COOKIES.get('uname')
    if uname is None:
        uname = ''
    # head为0,不显示顶栏,logo_search为0,不显示logo和搜索框
    context = {'title': '登录', 'head': 0, 'logo_search': 0,'uname':uname}
    return render(request, 'user/login.html', context)


def user_center_site(request):
    # head为0,不显示顶栏;logo_search为0,不显示logo和搜索框,1为搜索框在中间，2为搜索框在右边
    context = {'title': '用户中心', 'head': 1, 'logo_search': 2}
    return render(request, 'user/user_center_site.html', context)


# 登录校验
def login_check(request):
    # head为0,不显示顶栏
    context = {'head':0}
    args = request.POST
    remember = args.get('user_remember',0)  # default记住用户名为0,即不记住
    uname = args.get('username').decode()
    passwd = args.get('pwd').decode()
    # print(uname, passwd)
    # 校验用户名密码是否为空
    if uname and passwd:
        # 不为空时
        user = UserInfo.objects.filter(username=uname)
        # 校验用户名是否存在
        if len(user):
            # 校验密码是否正确
            s1 = sha1()
            s1.update(passwd)
            up_pwd = s1.hexdigest()
            if user[0].passwd != up_pwd:
                context['error_pwd'] = '密码不正确'
                context['uname'] = uname
                return render(request,'user/login.html',context)
            else:
                response = redirect('/index/')
                # 用户名密码均正确，登录成功
                if remember == '1':
                    response.set_cookie('uname',uname,expires=datetime.datetime.now()+datetime.timedelta(days=14))
                else:
                    response.set_cookie('uname',uname,max_age=-1)
                return response
        else:
            context['error_name'] = '用户不存在'
            return render(request, 'user/login.html', context)
    elif uname:
        # 用户名不为空时
        context['error_pwd'] = '请输入密码'
        context['uname'] = uname
        return render(request, 'user/login.html', context)
    else:
        # 密码不为空时
        context['error_name'] = '请输入用户名'
        return render(request, 'user/login.html', context)

        # username:a
        # pwd:11111111
        # login_submit:登录


# cart购物车模块
def cart(request):
    # head为0,不显示顶栏
    context = {}
    context['head'] = 1
    return render(request, 'cart/cart.html')


# goods商品模块
def detail(request):
    # head为0,不显示顶栏
    context = {}
    context['head'] = 1
    return render(request, 'goods/detail.html')


# 商品列表页
def list(request):
    # head为0,不显示顶栏
    context = {}
    context['head'] = 1
    return render(request, 'goods/list.html')
