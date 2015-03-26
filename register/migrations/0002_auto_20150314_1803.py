# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=70, default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='flat',
            field=models.CharField(max_length=10, default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='house',
            field=models.CharField(max_length=10, default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(max_length=15, default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='street',
            field=models.CharField(max_length=100, default=123),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='activation_key',
            field=models.CharField(max_length=400),
            preserve_default=True,
        ),
    ]
