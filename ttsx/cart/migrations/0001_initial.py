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
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ccount', models.IntegerField()),
                ('cgood', models.ForeignKey(to='goods.GoodInfo')),
                ('cuser', models.ForeignKey(to='user.UserInfo')),
            ],
        ),
    ]
