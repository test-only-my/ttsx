# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiverInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('detail_address', models.CharField(max_length=200)),
                ('post_code', models.IntegerField()),
                ('tel', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('passwd', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=50)),
                ('tel', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
