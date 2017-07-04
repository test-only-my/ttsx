# coding=utf-8
from django.db import models

# Create your models here.


# 用户信息表，与收件人信息表是一对多关系
class UserInfo(models.Model):
    username = models.CharField(max_length=30)  # 用户名
    passwd = models.CharField(max_length=32)  # 密码
    email = models.CharField(max_length=50)  # 邮箱
    tel = models.IntegerField(null=True, blank=True)  # 联系方式
    address = models.CharField(max_length=200)  # 地址


# 收件人信息表
class ReceiverInfo(models.Model):
    name = models.CharField(max_length=30)  # 收件人姓名
    detail_address = models.CharField(max_length=200)  # 详细地址
    post_code = models.IntegerField()  # 邮编
    tel = models.IntegerField()  # 手机号
    user_belong = models.ForeignKey('UserInfo')  # 关联用户表
