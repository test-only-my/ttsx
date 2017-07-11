# coding=utf-8
import re

import datetime
from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render, redirect
from hashlib import sha1
# Create your views here.
from django.utils.timezone import now

import decorator
from goods.models import GoodInfo
from user.models import UserInfo, ReceiverInfo

# user用户模块
# 注册页面展示
def register(request):
    # head为0,不显示顶栏
    context = {'title': '注册', 'head': 0}
    return render(request, 'register.html', context)
# 注册判重校验
def register_again(request, args):
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
    re1 = '^[a - z0 - 9]'
    context = {
        'title': '注册',
        'uname': uname,
        'passwd': passwd,
        'passwd_confirm': passwd_confirm,
        'uemail': uemail
    }
    if len(uname) < 5 or len(uname) > 20:
        context['error_name'] = '请输入5-20个字符的用户名'
        return render(request, 'register.html', context)
    elif len(passwd) < 8 or len(passwd) > 20:
        context['error_pwd'] = '密码最少8位，最长20位'
        return render(request, 'register.html', context)
    elif re.match(re1, uemail) == None:
        context['error_email'] = '你输入的邮箱格式不正确'
        return render(request, 'register.html', context)
    elif allow != 'on':
        context['error_allow'] = '请勾选同意'
        return render(request, 'register.html', context)
    else:
        user = UserInfo()
        user.username = uname
        user.email = uemail
        # 密码加密
        s1 = sha1()
        s1.update(passwd)  # python3中需要把passwd先encode
        upwd_sha1 = s1.hexdigest()
        user.passwd = upwd_sha1
        user.save()
        return redirect('/user/login/')


# 登录页面展示
def login(request):
    # 如果cookie中有值，进入login页面，直接拿到显示在登录页面上
    uname = request.COOKIES.get('uname')
    if uname is None:
        uname = ''
    # head为0,不显示顶栏,logo_search为0,不显示logo和搜索框
    context = {'title': '登录', 'head': 0, 'logo_search': 0, 'uname': uname}
    return render(request, 'login.html', context)
# 登录校验
def login_check(request):
    # head为0,不显示顶栏
    context = {'head': 0}
    args = request.POST
    remember = args.get('user_remember', 0)  # default记住用户名为0,即不记住
    uname = args.get('username','').decode()
    passwd = args.get('pwd','').decode()
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
                return render(request, 'login.html', context)
            else:
                if not request.session.has_key('url_path'):
                    response = redirect('/goods/index/')  # request.session['url_path']
                else:
                    response = redirect(request.session.get('url_path'))
                # 取登录后的用户存储session，用于登录后的显示
                request.session['uid'] = user[0].id
                request.session['uname'] = user[0].username
                # print(user[0].id)
                # 用户名密码均正确，登录成功
                if remember == '1':
                    response.set_cookie('uname', uname, expires=datetime.datetime.now() + datetime.timedelta(days=14))
                else:
                    response.set_cookie('uname', uname, max_age=-1)
                return response
        else:
            context['error_name'] = '用户不存在'
            return render(request, 'login.html', context)
    elif uname:
        # 用户名不为空时
        context['error_pwd'] = '请输入密码'
        context['uname'] = uname
        return render(request, 'login.html', context)
    else:
        # 密码不为空时
        context['error_name'] = '请输入用户名'
        return render(request, 'login.html', context)
# 退出登录
def logout(request):
    request.session.flush()
    return redirect('/user/login/')

# 个人信息页面
@decorator.islogin
def user_center_info(request):
    goods = []
    # 取出cookie中的浏览记录，如果不存在，默认值为空，也不会报错
    see_goods = request.COOKIES.get('see_goods','').split(",")  # 最后一个分割出来的是空‘’
    # 遍历分割好的列表，如果存在该商品，记录到另一个列表中，不存在就什么也不做
    for see in see_goods:
        if see:
            see_good = GoodInfo.objects.get(id=int(see))
            goods.append(see_good)
    user = UserInfo.objects.filter(id=request.session.get('uid'))
    context = {'title': '用户中心', 'head': 1,'logo_search':2,'user':user[0],'goods':goods}
    return render(request, 'user_center_info.html', context)
# 收货地址页面
@decorator.islogin
def user_center_site(request):
    # head为0,不显示顶栏;logo_search为0,不显示logo和搜索框,1为搜索框在中间，2为搜索框在右边
    user = UserInfo.objects.filter(id=request.session.get('uid'))
    receives = ReceiverInfo.objects.filter(user_belong=user[0])  # 获取当前用户的收件人信息
    context = {'title': '用户中心', 'head': 1, 'logo_search': 2,'receives':receives}
    return render(request, 'user_center_site.html', context)
# 添加收件人信息
@decorator.islogin
def add_receive(request):
    # 获取当前用户，列表形式
    user = UserInfo.objects.filter(id=request.session.get('uid'))
    # 获取页面传的值
    args = request.POST
    name = args.get('name')
    detail_address = args.get('detail_address')
    post_code = args.get('post_code')
    tel = args.get('tel')
    # 创建一个对象，添加收件人地址
    receive = ReceiverInfo()
    receive.name = name
    receive.post_code = post_code
    receive.detail_address = detail_address
    receive.tel = tel
    receive.user_belong = user[0]
    receive.save()
    # return render(request,'user/user_center_site.html')
    return redirect('/user/user_center_site/')
# 所有订单页面
@decorator.islogin
def user_center_order(request):
    context = {'title':'用户中心','head':1,'logo_search':2}
    return render(request, 'user_center_order.html', context)






