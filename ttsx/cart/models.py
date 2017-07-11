from django.db import models

# Create your models here.
from user.models import UserInfo
from goods.models import GoodInfo


class CartInfo(models.Model):
    cuser = models.ForeignKey(UserInfo)
    cgood = models.ForeignKey(GoodInfo)
    ccount = models.IntegerField()
