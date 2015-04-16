# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20150314_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='first_name',
            field=models.CharField(max_length=100, default=123),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinfo',
            name='last_name',
            field=models.CharField(max_length=100, default=123),
            preserve_default=False,
        ),
    ]
