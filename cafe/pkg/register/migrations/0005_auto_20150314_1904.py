# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20150314_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
