# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_receiverinfo_user_belong'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiverinfo',
            name='post_code',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='receiverinfo',
            name='tel',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='passwd',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='tel',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
