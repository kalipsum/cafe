# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20150314_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=75)),
                ('city', models.CharField(max_length=70)),
                ('street', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=10)),
                ('flat', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='flat',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='house',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='street',
        ),
    ]
