# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gname', models.CharField(max_length=20)),
                ('gimg', models.ImageField(upload_to=b'goods/')),
                ('gprice', models.DecimalField(max_digits=6, decimal_places=2)),
                ('gclick', models.IntegerField()),
                ('gunit', models.CharField(max_length=10)),
                ('isDelete', models.BooleanField(default=False)),
                ('glong_name', models.CharField(max_length=200)),
                ('gstock', models.IntegerField(default=100)),
                ('gdetail', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='GoodType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tname', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodinfo',
            name='gtype',
            field=models.ForeignKey(to='goods.GoodType'),
        ),
    ]
