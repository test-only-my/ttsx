# coding=utf-8
from django.db import models

# Create your models here.
from goods.models import GoodInfo
from user.models import UserInfo


class OrderInfo(models.Model):
    id = models.IntegerField(primary_key=True)  # 日期时间+用户id
    odatetime = models.DateTimeField(auto_now_add=True)
    ototalprice = models.DecimalField(max_digits=9,decimal_places=2)
    ouser = models.ForeignKey(UserInfo)


class OrderDetail(models.Model):
    ogprice = models.DecimalField(max_digits=5,decimal_places=2)  # 有可能价格会变，比如优惠活动
    ogcount = models.IntegerField()  # 每件商品的数量
    oorder = models.ForeignKey(OrderInfo)
    ogoods = models.ForeignKey(GoodInfo)
