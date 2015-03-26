# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20150314_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='order',
            field=models.ForeignKey(blank=True, to='orders.Order', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
