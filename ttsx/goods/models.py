# coding=utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class GoodType(models.Model):
    tname = models.CharField(max_length=20)  # 类型名
    isDelete = models.BooleanField(default=False)  # 逻辑删除，默认不删除

    def __str__(self):
        return self.tname.encode('utf-8')


class GoodInfo(models.Model):
    gname = models.CharField(max_length=20)  # 名字
    gimg = models.ImageField(upload_to='goods/')
    gprice = models.DecimalField(max_digits=6,decimal_places=2)  # 单价
    gclick = models.IntegerField()  # 点击量
    gunit = models.CharField(max_length=10)  # 单位
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    glong_name = models.CharField(max_length=200)  # 副标题
    gstock = models.IntegerField(default=100)  # 库存
    gdetail = HTMLField()  # 富文本编辑器
    gtype = models.ForeignKey('GoodType')  # 外键，多类，与GoodType一对多

