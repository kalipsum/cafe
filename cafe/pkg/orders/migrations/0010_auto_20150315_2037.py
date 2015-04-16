# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kitchen', '0020_delete_basket'),
        ('orders', '0009_auto_20150314_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='name',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='price',
        ),
        migrations.RemoveField(
            model_name='basket',
            name='user',
        ),
        migrations.AddField(
            model_name='basket',
            name='dish',
            field=models.ForeignKey(default=2, to='kitchen.Dish'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
