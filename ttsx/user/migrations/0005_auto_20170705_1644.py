# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20170705_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(default=b' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tel',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
