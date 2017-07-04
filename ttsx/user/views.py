# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from user.models import UserInfo

# 首页
def index(request):
    return render(request,'index.html')


# user用户模块
# 注册页面展示
def register(request):
    return render(request,'user/register.html')

# 注册过程校验
def register_user(request):
    args = request.POST
    passwd = args.get('pwd')
    passwd_confirm = args.get('cpwd')
    allow = args.get('allow')
    if passwd != passwd_confirm or allow != 'on':
        return HttpResponse('Fiddren')
    else:
        user = UserInfo()
        user.username = args.get('user_name')
        user.passwd = passwd
        user.email = args.get('email')
        user.save()
        return HttpResponse('注册成功')

# 登录页面展示
def login(request):
    return render(request,'user/login.html')

# 登录校验
def login_check(request):
    args = request.POST
    uname = args.get('username').decode()
    passwd = args.get('pwd').decode()
    print(uname,passwd)
    # 校验用户名密码是否为空
    if uname and passwd:
        user = UserInfo.objects.filter(username=uname)
        print(user)
        # 校验用户名是否存在
        if user:
            # 校验密码是否正确
            if user.passwd != passwd:
                return HttpResponse('密码错误')
            else:
                return HttpResponse('登录成功')
        else:
            return HttpResponse('用户不存在')
    else:
        return HttpResponse('请输入用户名密码')

    # username:a
    # pwd:11111111
    # login_submit:登录


# cart购物车模块
def cart(request):
    return render(request, 'cart/cart.html')


# goods商品模块
def detail(request):
    return render(request, 'goods/detail.html')
def list(request):
    return render(request, 'goods/list.html')