# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20170705_1644'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ogprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('ogcount', models.IntegerField()),
                ('ogoods', models.ForeignKey(to='goods.GoodInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('odatetime', models.DateTimeField(auto_now_add=True)),
                ('ototalprice', models.DecimalField(max_digits=9, decimal_places=2)),
                ('ouser', models.ForeignKey(to='user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='oorder',
            field=models.ForeignKey(to='order.OrderInfo'),
        ),
    ]
