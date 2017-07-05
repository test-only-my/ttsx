# coding=utf-8
from django.db import models

# Create your models here.


# 用户信息表，与收件人信息表是一对多关系
class UserInfo(models.Model):
    username = models.CharField(max_length=30)  # 用户名
    passwd = models.CharField(max_length=40)  # 密码sha1加密
    email = models.CharField(max_length=50)  # 邮箱
    tel = models.CharField(default='',max_length=20)  # 联系方式
    address = models.CharField(max_length=200,default=' ')  # 地址


# 收件人信息表
class ReceiverInfo(models.Model):
    name = models.CharField(max_length=30)  # 收件人姓名
    detail_address = models.CharField(max_length=200)  # 详细地址
    post_code = models.CharField(max_length=6)  # 邮编
    tel = models.CharField(max_length=20)  # 手机号
    user_belong = models.ForeignKey('UserInfo')  # 关联用户表
