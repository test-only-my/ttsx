# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20170704_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiverinfo',
            name='user_belong',
            field=models.ForeignKey(default=1, to='user.UserInfo'),
            preserve_default=False,
        ),
    ]
